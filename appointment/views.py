from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
def details(request):
    if request.method=='POST': 
        print(request.body)
        fullname = request.POST['fullname']
        phone = request.POST['phone']
        email = request.POST['email']
        date = request.POST['date']
        subject = request.POST['subject']
        user = Appointment.objects.create( fullname=fullname, phone=phone, email=email, date=date,subject=subject)
        user.save()
    return HttpResponse("Successfully submitted", status=200)
