from django.urls import path
from todoapp import views

urlpatterns=[

path("signup/",views.SignUpView.as_view(), name="register"),
path("",views.SignInView.as_view(), name="login"),
path("home/",views.IndexView.as_view(), name="index"),
path("signout/",views.SignOutView.as_view(), name="signout"),



]