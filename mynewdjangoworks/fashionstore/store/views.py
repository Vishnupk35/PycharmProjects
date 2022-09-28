from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import products
#store/products/
class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        if "rate" in request.query_params:
            rating=float(request.query_params.get("rate"))
            sort_rating=[rat for rat in products if rat["rating"]["rate"]>=rating]
            return Response(data=sort_rating)
        else:
            return Response(data=products)
