# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - employee-onboarding
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Profile, EmployeeDocuments
from .forms import SignUpForm
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry

# Register your models here.

@admin.register(EmployeeDocuments)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile','file_name')
    list_per_page = 10
# admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_per_page = 10

class AuthorAdmin(admin.ModelAdmin):
    form = SignUpForm

admin.site.register(User, AuthorAdmin)
admin.site.unregister(Group)
class AuthorAdmin1(admin.ModelAdmin):
    list_display = ('id', 'user')

admin.site.register(LogEntry, AuthorAdmin1)

