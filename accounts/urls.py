# accounts/urls.py
from django.urls import path

from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", views.profile, name="profile"),
    path("destroy/", views.destroy, name="destroy_user"),
]
