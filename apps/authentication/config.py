# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - employee-onboarding
"""

from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'apps.authentication'
    label = 'apps_authentication'
    
    def ready(self):
        import apps.authentication.signals
