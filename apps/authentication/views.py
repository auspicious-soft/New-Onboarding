# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - employee-onboarding
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from apps.authentication.models import Profile
from .forms import LoginForm
from django.http import HttpResponseRedirect
# from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                if user.is_superuser is True:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    login(request, user)
                    return redirect('/')
        else:
            form = LoginForm()
        return render(request, "accounts/login.html", {'form': form})


# class LoginView(APIView):
#     def post(self, request, format=None):
#         data = request.data

#         username = data.get('username', None)
#         password = data.get('password', None)

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 if user.is_superuser is True:
#                     login(request, user)
#                     return redirect("dashboard")
#                 else:
#                     login(request, user)
#                 return Response(status=status.HTTP_200_OK)
#             else:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)


@login_required(login_url="/login")
def user_logout(request):
    logout(request)
    return redirect('login')   



# def register_user(request):
#     msg = None
#     success = False

#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)

#             msg = 'User created successfully.'
#             success = True

#             # return redirect("/login/")

#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()

#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

# def setting_update(request):
    
#     # if request.method == 'POST':
#     #     form = SettingForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         print("created..!")

#     # else:
#     #     form = SettingForm()
       
#     return render(request,"accounts/account-setting.html",{'form':form})


#  This is view Profile View 
# class SettingsView(View):
#     form_class = SettingForm
#     template_name = 'accounts/account-setting.html'
    
#     def get(self,request):
#         data = Profile.objects.filter(user=request.user).first()
#         context = {'data':data}
#         return render(request, self.template_name, context)
    
#     def post(self,request):
#         data = User.objects.get(id=request.user.id)
#         form = self.form_class(request.POST, instance=data)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, "Profile updated successfully.")
#             return redirect("/setting_update")
#         return render(request,self.template_name, {'form': form})