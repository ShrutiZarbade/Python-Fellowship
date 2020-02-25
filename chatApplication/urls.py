from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.Registration.as_view(), name='register'),
    path("activate/<token>", views.activate, name='activate'),
    path("login/", views.Login.as_view(), name='login'),
    path("logout/", views.Logout.as_view(), name='logout'),
    path("forgot/", views.Logout.as_view(), name='forgot'),
    path("reset/<token>", views.ForgotPassword.as_view(), name='reset'),
]


