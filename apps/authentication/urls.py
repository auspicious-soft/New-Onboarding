# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - employee-onboarding
"""

from django.urls import path
# from .views import login_form_view, LoginView
# from django.contrib.auth.views import LogoutView
from apps.authentication import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    # path('api/login', LoginView.as_view(), name="login_api"),
    # path("logout/", LogoutView.as_view(), name="logout"),
    path('logout/', views.user_logout, name='logout_user'),
    # path('setting_update',SettingsView.as_view(),name='setting_update')
]
