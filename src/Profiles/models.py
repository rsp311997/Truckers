import profile
from tkinter import CASCADE
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validateMobile(value):
    if len(value) != 10:
        raise ValidationError(_('Mobile number must be of 10 digits.'),params={'value':value})

def validateRole(value):
    roles=['trucker','customer','transpoter']
    if value not in roles:
        raise ValidationError(_('Specified role is Invalid.'),params={'value':value})

class Profile(models.Model):
    mobile=models.CharField(max_length=10,unique=True,blank=False,null=False,validators=[validateMobile])
    profileImg=models.ImageField(blank=False,null=False)
    role=models.CharField(max_length=50,blank=False,null=False,validators=[validateRole])
    userID=models.OneToOneField(to=User,unique=True,blank=False,null=False,on_delete=models.CASCADE,related_name="_Profile")
    
class LicenseImage(models.Model):
    licenseImg=models.ImageField(blank=False,null=False)
    profileID=models.OneToOneField(to=Profile,unique=True,blank=False,null=False,on_delete=models.CASCADE,related_name="_LicenseImg")

