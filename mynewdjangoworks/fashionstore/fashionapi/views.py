from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from functools import reduce

# Create your views here.
class HelloWorldView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Helloworld"})

class GreetingsView(APIView):
    def get(self,request,*args,**kwargs):
        msg=""
        c_date=datetime.datetime.now()
        c_hour=c_date.hour
        if c_hour<12:
            msg="Good morning"
        elif c_hour<18:
            msg="Good afternoon"
        elif c_hour<24:
            msg="Good night"
        return Response({"data":msg})

class AddNumbersView(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})

class SubNumbersView(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response({"msg":res})
class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        res=n**3
        return Response({"msg":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        num=request.data.get("num")
        fact=reduce(lambda n1,n2:n1*n2,range(1,num+1))
        return Response({"msg":fact})


class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        wc={}
        words=text.split(" ")
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response({"data":wc})


