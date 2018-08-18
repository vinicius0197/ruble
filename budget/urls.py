from django.urls import path
from . import views

urlpatterns = [
    path("<dash_id>", views.dashboard, name="dashboard")
]