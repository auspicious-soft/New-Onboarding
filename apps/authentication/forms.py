# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - employee-onboarding
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from apps.authentication.models import Profile
User = get_user_model()

from django.contrib.auth import authenticate



class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}), label='Password')
    
    class Meta:
        model = User
        fields = ('username','password')


    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username,password=password):
                raise forms.ValidationError("Incorrect Username / Password please try again.")



    def get_user(self):
   
        return authenticate(
                username=self.cleaned_data.get('username', '').lower().strip(),
                password=self.cleaned_data.get('password', ''),
        )        


class SignUpForm(UserCreationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class SettingForm(forms.ModelForm):
    
    # COUNTRY = (('United States','United States'),
    #             ('Germany','Germany'),
    #             ('France', 'France'), 
    #             ('Spain','Spain'),
    #             ('Italy', 'Italy'),
    #             ('Russia','Russia'), 
    #             ('Japan', 'Japan'), 
    #             ('India','India'),
    #             ('China', 'China'))
      
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Enter your first name",
    #             "class": "form-control"
    #         }))
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Enter your last name",
    #             "class": "form-control"
    #         }))
   
    # birthday = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Enter your last name",
    #             "class": "form-control"
    #         }))
    # phone = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Enter your phone",
    #             "class": "form-control"
    #         }
    #     ))
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "placeholder": "Enter your email",
    #             "class": "form-control"
    #         }
    #     ))
    # address = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Enter your address",
    #             "class": "form-control"
    #         }
    #     ))

    # city = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Enter your city",
    #             "class": "form-control"
    #         }))
    # country = forms.ChoiceField(
    #             widget=forms.Select(
    #                 attrs={'class': 'form-control'}),
    #                 choices=COUNTRY)
    
    # image = forms.ImageField(required=False,
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Image",
    #             "class": "form-control"
    #         }))
    
    class Meta:
        model = Profile
        fields = "__all__"