from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import blogs,users


class PostView(APIView):
    def get(self,request,*args,**kwargs):
        if "liked_by" in request.query_params:
            id=int(request.query_params.get("liked_by"))
            liked_post=[blog for blog in blogs if id in blog["liked_by"]]
            return Response(data=liked_post)
        else:
            return Response({"data":blogs})

        # http://127.0.0.1:8000/social/posts/{pid}
        # method: post
        # data:{"postId": 9, "userId": 6, "title": "hai hello", "content": "new content"
    def post(self, request, *args, **kwargs):
        blog = request.data
        blogs.append(blog)
        return Response(data=blog)


#http://127.0.0.1:8000/social/posts/{pid}
#method: get
class PostDetailView(APIView):
    def get(self,request,*args,**kwargs):
        post_id=kwargs.get("pid")
        post=[p for p in blogs if p["postId"]==post_id].pop()
        return Response(data=post)

    # http://127.0.0.1:8000/social/posts/{pid}
    # method: delete
    def delete(self,request,*args,**kwargs):
        post_id = kwargs.get("pid")
        post = [p for p in blogs if p["postId"] == post_id].pop()
        blogs.remove(post)
        return Response(data=post)

    def put(self,request,*args,**kwargs):
        post_id = kwargs.get("pid")
        post = [p for p in blogs if p["postId"] == post_id].pop()
        post.update(request.data)
        return Response(data=post)
#http://127.0.0.1:8000/social/posts/likes/<int:post_id>
    # method: post
    # data: {"user_id":1}
class AddLikeView(APIView):
    def post(self,request,*args,**kwargs):
        post_id = kwargs.get("post_id")
        id=request.data.get("user_id")
        post = [p for p in blogs if p["postId"] == post_id].pop()
        post["liked_by"].append(id)
        return Response(data=post)