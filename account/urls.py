from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views

urlpatterns = [
    path('',  views.dashboard, name='dashboard'),
    # path('login/', views.user_login, name='login'),
    path('login/', LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView, name='password_change'),
    path('password-change/done/', PasswordChangeDoneView, name='password_change_done'),
    # TODO: create custom login view based on django.contrib.auth.views.LoginView
    # TODO: create custom logout view based on django.contrib.auth.views.LogoutView
    # TODO: read about password reset
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
