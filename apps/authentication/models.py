# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - employee-onboarding
"""

from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.contrib.auth.models import PermissionsMixin
import uuid
import os

USERS_ROLES = (
    ("ADMIN", 1),
    ("EMPLOYEE",  2))

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username        =   models.CharField(max_length=64, unique=True)
    email           =   models.EmailField(unique=True,  null=True,  blank=True)
    role            =   models.IntegerField(default=2,  choices=USERS_ROLES)
    status          =   models.BooleanField(default=True)

    is_staff        =   models.BooleanField(default=False)
    is_superuser    =   models.BooleanField(default=False)

    date_created    =   models.DateTimeField(auto_now_add=True)
    date_modified   =   models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        role = "Admin"
        if self.role == 2:
            role = "Employee"
        return f"Username : {self.username},  Role : {role}"


class Profile(models.Model):
    id              =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user            =   models.ForeignKey(User, related_name="user_profile",   on_delete=models.CASCADE)
    # image           =   models.ImageField(
    #                         upload_to='profile_pic', 
    #                         default='/static/assets/img/profile-picture-3.jpg')
    abn             =   models.CharField(max_length=100,  null=True,  blank=True)
    bussiness_name  =   models.CharField(max_length=64,   null=True,  blank=True)
    first_name      =   models.CharField(max_length=64,   null=True,  blank=True)
    middle_name     =   models.CharField(max_length=64,   null=True,  blank=True)
    last_name       =   models.CharField(max_length=64,   null=True,  blank=True)
    birthday        =   models.DateField(null=True,       blank=True)

    # address details
    search_address  =   models.CharField(max_length=500,  null=True,  blank=True)
    street_address  =   models.CharField(max_length=100,  null=True,  blank=True)
    number          =   models.IntegerField(null=True,    blank=True)
    city            =   models.CharField(max_length=100,  null=True,  blank=True)
    country         =   models.CharField(max_length=100,  null=True,  blank=True)

    # account details
    bsb             =   models.CharField(max_length=50,  null=True,  blank=True)
    account_number  =   models.IntegerField(null=True,  blank=True)
  
    date_created    =   models.DateTimeField(auto_now_add=True)
    date_modified   =   models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return "Username={}, FirstName={}".format(
    #         self.user.username,
    #         self.first_name)


class EmployeeDocuments(models.Model):
    profile         =   models.ForeignKey(Profile,      on_delete=models.CASCADE)
    number          =   models.IntegerField(null=True,  blank=True)
    expiry_date     =   models.DateField(null=True,  blank=True)
    issue_date      =   models.DateField(null=True,  blank=True)
    file_name       =   models.CharField(max_length=30) 
    file            =   models.FileField(upload_to=os.path.join('uploads','EmployeeDocuments'))
    
    date_created    =   models.DateTimeField(auto_now_add=True)
    date_modified   =   models.DateTimeField(auto_now=True)


    def __str__(self):
        return "Profile={}, Number={}".format(
            self.profile.id,
            self.number)