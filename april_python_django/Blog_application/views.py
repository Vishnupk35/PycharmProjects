from Blog_application.Model1 import users,posts
session={}
#authenticate
# username="anu"
# password="Password@123"
# user = [user for user in users if user["username"] == username and user["password"] == password]
# print(user) or
# def authenticate(username,password):
#     user = [user for user in users if user["username"] == username and user["password"] == password]
#     return user
# print(authenticate("anu","Password@123"))

def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user

def SignInRequired(fn):
    def wrapper(*args, **kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("You must log-in ")
    return wrapper
#get>> retrieve
#post>>create
#put/patch>>edit
#delete>>delete

class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("success")
            print(session)
        else:
            print("invalid")
class PostView:
    @SignInRequired
    def get(self,*args,**kwargs):
        return posts

    @SignInRequired
    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        posts.append(kwargs)
        print(posts)

class MyPostlistView:
    @SignInRequired
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts
class PostsDetailsView:

    def get_object(self,id):
        post=[post for post in posts if post["postId"] ==id]
        return post

    @SignInRequired
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=kwargs.get("data")
        instance=self.get_object(post_id)
        if instance:
            post_obj=instance[0]
            post_obj.update(data)
            return post_obj
        else:
            print("post not found to update")

    @SignInRequired
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=self.get_object(post_id)
        return post

    @SignInRequired
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=[post for post in posts if post["postId"]==post_id]
        if data:
            post=data[0]
            posts.remove(post)
            print("Post removed successfully")
            print(len(posts))
class LikeView:
    @SignInRequired
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=[post for post in posts if post["postId"]==post_id]
        user_id=session["user"]["id"]
        if post:
            post=post[0]
            post["liked_by"].append(user_id)
            print(post)
            print(len(post["liked_by"])," people liked the post")
        else:
            print("Post not found")
@SignInRequired
def sign_out(*args,**kwargs):
    user=session.pop("user")
    print(f"{user['username']} logged out successfully")

log=SignInView()
log.post(username="anu",password="Password@123")

like=LikeView()
like.get(post_id=5)
sign_out()
# mypost=MyPostlistView()
# print(mypost.get())
# post_detail=PostsDetailsView()
# post_detail.delete(post_id=6)
# print(post_detail.get(post_id=3))
# data={"title":"Hello friends"}
# post_detail.put(post_id=3,data=data)




# data=PostView()
# data.post(postId=9,
#           title="good morning",
#           content="morning coffee",
#           liked_by=[])
