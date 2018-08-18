from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class DashboardId(models.Model):
    def generate_custom_id():
        """ Generates a random string for each user budget dashboard """
        string = get_random_string(length=32)
        if DashboardId.objects.filter(dashboard_id = string).exists():
            while DashboardId.objects.filter(dashboard_id = string).exists() == True:
                string = get_random_string(length=32)
        
        return string

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dashboard_id = models.CharField(settings.AUTH_USER_MODEL, max_length=32, default=generate_custom_id)