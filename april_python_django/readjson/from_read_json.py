from json import *
f=open("blog.json")
with open("blog.json") as f:
    data=load(f)
print(data)
#no:of posts by user
user_posts=[post for post in data if post["userId"]==1]
print(len(user_posts))
#no:of likes for postid=3

likes=[len(post["liked_by"]) for post in data if post["postId"]==3]
print(likes)
#posts liked by id2
like_id2=[post for post in data if 2 in post["liked_by"]]
print(len(like_id2))
#most liked post
most_like=max(data, key=lambda post:len(post["liked_by"]))
print(most_like)