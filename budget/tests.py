from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from users.models import DashboardId

class DashboardTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {
            "username": "test_user",
            "email": "test@email.com",
            "password": "test_password"
        }
        # Create mock data
        self.user = User.objects.create_user(**self.credentials)
        DashboardId.objects.create(user=self.user)

    def test_user_is_redirected(self):
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/users', follow=True)

        self.assertEqual(response.status_code, 200)