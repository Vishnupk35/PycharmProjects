from django.shortcuts import render
from django.views.generic import View
from social import templates

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")
        pass
    def post(self,request,*args,**kwargs):
        pass
class RegisterView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"register.html")