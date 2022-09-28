from blog.Models import users,posts


# authenticate
def authenticate(**kwargs):
    username=kwargs.get("username")
    email=kwargs.get("email")
    user_data=[user for user in users if user["username"]==username and user["email"]==email]
    return user_data
    # if user_data
session={}

class SignInView:

    def post(self,*args, **kwargs):
        username = kwargs.get("username")
        email=kwargs.get("email")
        user=authenticate(username=username,email=email)
        if user:
            print("Login Success")
            session["user"]=username
        else:
            print("Invalid credentils")

def login_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("You must login")
    return wrapper
@login_required
def logged_user():
    username=session.get("user")
    user_id=[user["id"] for user in users if user["username"]==username][0]
    return user_id
@login_required
def logout(*args,**kwargs):
    session.pop("user")
    print("user logged out")

class PostListView:
    @login_required
    def get(self,*args,**kwargs):
        return posts
# design pattern
# decorators
class MyPostsView:

    @login_required
    def get(self,*args,**kwargs):
        user_id=logged_user()
        qs=[post for post in posts if post["userId"]==user_id]
        return qs

class PostCreateView:
    def post(self,*args,**kwargs):
        user_id=logged_user()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":user_id,
            "title":title,
            "body":body
        }
        posts.append(data)
        print("post created successfully")

class PostDetailsView:
    @login_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        qs=[p for p in posts if p.get("id")==post_id]
        return qs

    def put(self,id=None,*args,**kwargs):
        post=[p for p in posts if p.get("id")==id][0]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"]=body
        print(post)


user=SignInView()
user.post(username="django",email="django@gmail.com")
pst=PostCreateView()
pst.post(title="My Car",body="Hello friends, this is my new car")

mp=MyPostsView()
print(mp.get())

detail=PostDetailsView()
detail.put(id=10,title="My new post",body="Hello friends, my new post is")

