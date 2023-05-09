# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - employee-onboarding
"""
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import pytesseract
from PIL import Image
from django.views import View
from django.http import JsonResponse
from pytesseract import Output
from apps.authentication.models import Profile, EmployeeDocuments
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    profile = Profile.objects.get(user=request.user)
    context['profile'] = profile
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def dashboard(request):
    context = {'segment': 'dashboard'}
    # user_docs = EmployeeDocuments.objects.all().order_by('-id')
    user = User.objects.filter(is_superuser=False).order_by('-id')
    print(user)
    data = {}
    for u in user:
        context['user'] = u.username
        profile = Profile.objects.get(user=u)
        context['user_docs'] = EmployeeDocuments.objects.filter(profile=profile)
    # context['user_docs'] = user_docs
    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))


def EmployeeDocumentView(request):
    try:
        response_data = {}
        upload = request.FILES['file']
        custom_config = r'--oem 3 --psm 6'
        content = pytesseract.image_to_string(Image.open(upload), config=custom_config)
        # d = pytesseract.image_to_data(Image.open(upload), output_type=Output.DICT)
        # text = content.encode("ascii", "ignore")
        # text = text.decode()
        # Summary (0.1% of the original content).
        # summarized_text = summarize(text, ratio=0.1)
        html_string = f"<div class='content'>{content}</div>"
        response_data['content'] = html_string
        # response_data['text'] = text
        # response_data['summarized_text'] = summarized_text
        return JsonResponse(response_data, safe=True)
    except Exception as e:
        return JsonResponse({"massage":f"{str(e)}"},safe=True)

def get_FileName(numbers_list, expiry_date):
    count = 0
    file_names = []
    exp_date =[]
    numbers = []
    for n, date in zip(numbers_list, expiry_date):
        count = count +1
        if n == '':
            continue
        if count == 1:
            file_name = "crp_certificate"
        elif count == 2:
            file_name = "first_aid_certificate"
        elif count == 3:
            file_name = "insurance_certificate"
        elif count == 4:
            file_name = "agreement"
        file_names.append(file_name)
        exp_date.append(date)
        numbers.append(n)
    return file_names, exp_date, numbers

def uploadDocs(user, numbers, files, expiry_date, issue_date):
    file_names, exp_date, numbers = get_FileName(numbers, expiry_date)
    profile = Profile.objects.get(user=user)
    for num, name, date, file in zip(numbers, file_names, exp_date, files):
        
        if name == "crp_certificate":
            p, created = EmployeeDocuments.objects.get_or_create(
                profile = profile,
                number = num,
                expiry_date = date,
                file_name = name,
                file = file)
            print("===created",created)
        elif name == "first_aid_certificate":
            p, created = EmployeeDocuments.objects.get_or_create(
                profile = profile,
                number = num,
                expiry_date = date,
                issue_date = issue_date,
                file_name = name,
                file = file)
            print("===created",created)
        elif name == "insurance_certificate":
            p, created = EmployeeDocuments.objects.get_or_create(
                profile = profile,
                number = num,
                expiry_date = date,
                issue_date = issue_date,
                file_name = name,
                file = file)
            print("===created",created)
        elif name == "agreement":
            p, created = EmployeeDocuments.objects.get_or_create(
                profile = profile,
                number = num,
                expiry_date = date,
                issue_date = issue_date,
                file_name = name,
                file = file)
            print("===created",created)
    return True

class EmployeeUploadView(APIView):
    def post(self, request, format=None):
        data = request.data
        try:
            abn = data.get('abn')
            bussiness_name  = data.get('bussiness_name') 
            first_name  = data.get('first_name')
            middle_name = data.get('middle_name')
            last_name   = data.get('last_name')
            birthday    = data.get('birthday')
            search_address  = data.get('search_address')
            street_address  = data.get('street_address')
            # number  = data.get('number')
            city    = data.get('city')
            country = data.get('country')
            bsb = data.get('bsb')
            account_number  = data.get('account_number')
            
            number_list = request.POST.getlist('number[]')
           
            obj = Profile.objects.get(user=request.user)
            obj.abn  = abn
            obj.bussiness_name = bussiness_name
            obj.first_name = first_name
            obj.middle_name = middle_name 
            obj.last_name = last_name
            obj.birthday = birthday
            obj.search_address = search_address
            obj.street_address = street_address
            # obj.number = number
            obj.city = city
            obj.country = country
            obj.bsb = bsb
            obj.account_number = account_number
            obj.save()
            # save docs
            if len(number_list) > 0:
                files = request.FILES.getlist('file[]')
                expiry_date = request.POST.getlist('expiry_date[]')
                uploadDocs(request.user, number_list, files, expiry_date, data.get('issue_date'))
    
            return JsonResponse({"massage":"Profile Updated successfully."}, safe=True)
        except Exception as e:
            return JsonResponse({"massage":f"{str(e)}"}, safe=True)
            

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



