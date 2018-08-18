from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

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

    def test_signup_view(self):
        response = self.client.get('/users/signup', follow=True)

        self.assertEqual(response.status_code, 200)