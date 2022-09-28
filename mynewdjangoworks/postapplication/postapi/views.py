from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from postapi.serializers import UserSerializer,UserProfileSerializer,PostSerializer,CommentSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from postapi.models import UserProfile,Posts,Comments
from rest_framework.decorators import action

class UserRegistrationView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer=UserProfileSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    #api/v1/users/profile/{pk}/follow
    #requet.user=Mohanlal
    #pk=Asif
    @action(methods=["post"],detail=True)
    def follow(self,request,*args,**kwargs):
        id=kwargs.get("pk") #asif user id
        user_to_follow=User.objects.get(id=id) #asif object
        profile=UserProfile.objects.get(user=request.user) #Mohanlal user profile
        profile.following.add(user_to_follow) # Added asif(user_to_follow) to Mohanlal's following
        return Response({"msg":"followed"})

    # api/v1/users/profile/my_followings/
    @action(methods=["get"],detail=False)
    def my_followings(self,request,*args,**kwargs):
        get_followings=request.user.following.all()
        serializer=UserProfileSerializer(get_followings,many=True)
        return Response(data=serializer.data)



class PostView(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):#Override def perform_create from mixins
        serializer.save(author=self.request.user)
    #http://127.0.0.1:8000/api/v1/posts/{pid or pk}/add_comment
    @action(methods=["post"],detail=True)#custom method
    def add_comment(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        user=request.user
        serializer=CommentSerializer(data=request.data,context={"post":post,"user":user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    # http://127.0.0.1:8000/api/v1/posts/{pid or pk}/get_comments
    @action(methods=["get"],detail=True)
    def get_comments(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        post=Posts.objects.get(id=id)
        comments=post.comments_set.all()#post.comments.all --- This we can use if we set related name as comments for the post
        serializer=CommentSerializer(comments,many=True)
        return Response(data=serializer.data)

    # http://127.0.0.1:8000/api/v1/posts/{pid or pk}/add_like
    @action(methods=["post"],detail=True)
    def add_like(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        post = Posts.objects.get(id=id)
        post.liked_by.add(request.user)

        return Response({"message":"liked successfully"})


