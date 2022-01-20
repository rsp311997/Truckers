from asyncio import exceptions
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .forms import RegisterForm

# Create your views here.

#register
class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,"Register.html",context={'form':form})
    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create(username=form.cleaned_data['Username'],password=form.cleaned_data['Password'])
                user.set_password(user.password)
                user.first_name=form.cleaned_data['FirstName']
                user.last_name=form.cleaned_data['LastName']
                user.email=form.cleaned_data['Email']
                user.save()
                return redirect(to="login")
            except Exception as error:
                return render(request,"Register.html",context={'form':form,'error':f'Unable to create account : {error}'})
        return render(request,"Register.html",context={'form':form})
#login
class LoginView(View):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        pass
#logout
class LogoutView(View):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        pass
#Profile
class ProfileView(View):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        pass
    def put(self,request,*args,**kwargs):
        pass
#License
class LicenseImageView(View):
    def get(self,request,*args,**kwargs):
        pass
    def post(self,request,*args,**kwargs):
        pass
    def put(self,request,*args,**kwargs):
        pass