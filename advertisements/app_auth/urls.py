from django.urls import path
from .views import login_view, profile_view, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", login_view, name='login'),
    path("profile/", profile_view, name='profile'),
    path("register/", register_view, name='register'),
    path("logout/", auth_views.LogoutView.as_view(next_page='main-page'), name='logout'),
]
