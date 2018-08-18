from django.urls import include, path
from . import views

urlpatterns = [
    path('budget/', include('budget.urls')),
    path("", views.index, name="index"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
    path("signup", views.signup, name="signup")
]