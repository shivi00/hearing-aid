from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


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
        subject = 'Subject of the Email'
        message = 'Body of the email.'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['kiran04252@gmail.com']  # Replace with the recipient's email address
        send_mail(subject, message, from_email, to_email)
    return HttpResponse("Successfully submitted", status=200)
