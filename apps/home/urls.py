# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - employee-onboarding
"""

from django.urls import path
from apps.home import views
from .views import EmployeeDocumentView, EmployeeUploadView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('api/employee', views.EmployeeDocumentView, name="employee_document_api"),
    path('employee/upload', views.EmployeeUploadView.as_view(), name="employee_upload")

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages')
   

]
