from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

from .models import DashboardId

class AuthTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {
            "username": "test_user",
            "email": "test@email.com",
            "password": "test_password"
        }
        self.user = User.objects.create_user(**self.credentials)

    def test_login_view(self):
        response = self.client.get('/users/login', follow=True)
        login_sucessful = self.client.login(username="test_user", password="test_password")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(login_sucessful)

    def test_signup_view_loads(self):
        response = self.client.get('/users/signup', follow=True)

        self.assertEqual(response.status_code, 200)

    def test_signup_generates_random_id(self):
        response = self.client.post('/users/signup',
                                    {"username": "test",
                                    "email": "test@email.com" ,
                                    "password": "teste"}, follow=True)

        self.assertEqual(response.status_code, 200)

        # Make sure user is created
        user = User.objects.filter(username="test").exists()
        self.assertTrue(user)

        if user:
            user = User.objects.get(username="test")

        try:
            dash_id = user.dashboardid.dashboard_id
        except DashboardId.DoesNotExist:
            self.fail("signup() view failed to created dash_id. DashboardId.DoesNotExist")

        self.assertEqual(len(dash_id), 32)