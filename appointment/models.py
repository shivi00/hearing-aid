from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Appointment(models.Model):
    fullname = models.CharField(max_length=100,null=True)
    email= models.EmailField(max_length=100,null=True)
    phone    = models.CharField(max_length=50, null=True)
    subject= models.EmailField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.id)