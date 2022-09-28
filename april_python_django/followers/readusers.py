from json import *
with open("users.json") as f:
    data=load(f)
#followers of id2
followers_2=[len(i["followers"]) for i in data if i["id"]==2]
print(followers_2)
#users with most followers
max_followers=max(data,key=lambda user:len(user["followers"]))
print(max_followers)
#Suggestions to follow
all_users=[user["id"] for user in data]
print(all_users)
my_followings=[user["following"] for user in data if user["id"]==1][0]
print(my_followings)
check=[i for i in all_users if i not in my_followings]
print(check) #result in lst format
#or
check_better=set(all_users)-set(my_followings)
print(check_better) #Result in dic
