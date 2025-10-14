from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile_view, name="profile"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/edit/", views.edit_profile_view, name="edit_profile"),
    path("profile/erase/", views.erase_account_view, name="erase_account"),
]
