from django.shortcuts import render
from blogapi.models import Mobiles,Reviews,Cart
from rest_framework.views import APIView
from rest_framework.response import Response
from blogapi.serializers import MobileSerializer,MobileModelSerializer,UserSerializer,ReviewSerializer,CartSerializer
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from rest_framework.decorators import action
#http://127.0.0.1:8000/myg/mobiles/
#method: get
#list
#create
#http://127.0.0.1:8000/myg/mobiles/
#method: post
#detail
#update
#delete
class MobileView(APIView): #list http://127.0.0.1:8000/myg/mobiles/
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serialize=MobileSerializer(qs,many=True)
        return Response(data=serialize.data)

    def post(self,request,*args,**kwargs):
        serialize=MobileSerializer(data=request.data)
        if serialize.is_valid():
            Mobiles.objects.create(**serialize.validated_data)
            return Response(data=serialize.data)
        else:
            return Response(data=serialize.errors)

class MobileDetailView(APIView):#http://127.0.0.1:8000/myg/mobiles/{id}/
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            qs=Mobiles.objects.get(id=id)
            serialize=MobileSerializer(qs)
            return Response(data=serialize.data)
        except:
            return Response({"msg":"data not exist"},status=status.HTTP_404_NOT_FOUND)

    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        try:
            object = Mobiles.objects.get(id=id)
            serialize=MobileSerializer(data=request.data)
            if serialize.is_valid():
                object.name=serialize.validated_data.get("name")
                object.price=serialize.validated_data.get("price")
                object.band=serialize.validated_data.get("band")
                object.display=serialize.validated_data.get("display")
                object.processor=serialize.validated_data.get("processor")
                object.save()
                return Response(data=serialize.data)
        except:
            return Response({"msg": "data not exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        try:
            object=Mobiles.objects.get(id=id)
            object.delete()
            return Response({"msg":"data deleted"})
        except:
            return Response({"msg":"data not exist"},status=status.HTTP_404_NOT_FOUND)


class MobileModelsView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class MobileModelsDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return Response(data=serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance = Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs = Mobiles.objects.get(id=id)
        qs.delete()
        return Response({"msg":"deleted"})

class MobileViewSetView(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def create(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)
        qs.delete()
        return Response({"msg":"content deleted"})

class MobileModelViewSetView(viewsets.ModelViewSet):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MobileModelSerializer
    queryset = Mobiles.objects.all()
    #api/v4/myg/mobiles/{pid"/add_review
    #method: post
    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        mobile=Mobiles.objects.get(id=id)
        user=request.user
        serializer=ReviewSerializer(data=request.data,context={"user":user,"product":mobile})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    # api/v4/myg/mobiles/{pid}/get_review
    # method: get
    @action(methods=["get"],detail=True)
    def get_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        mobile=Mobiles.objects.get(id=id)
        reviews=mobile.reviews_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)

    #api/v4/mobiles/{pid}/add_to_cart
    # method: post
    @action(methods=["post"],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        user=request.user
        id=kwargs.get("pk")
        mobile=Mobiles.objects.get(id=id)
        cart=Cart.objects.filter(user=user,product=mobile)
        if cart:
            object=cart[0]
            object.quantity+=1
            object.save()
            return Response({"msg":"ok"})

        else:
            serializer=CartSerializer(data=request.data, context={"user":user,"product":mobile})
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
    @action(methods=["get"],detail=False)
    def my_cart(self,request,*args,**kwargs):
        qs=Cart.objects.filter(user=request.user)
        serializer=CartSerializer(qs,many=True)
        return Response(data=serializer.data)

class CartsView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(data=self.request.user)

    # def get_queryset(self):
    #     return Cart.objects.filter(data=self.request.user)

#api/v4/myg/mobiles/cart
class UserRegistrationView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


