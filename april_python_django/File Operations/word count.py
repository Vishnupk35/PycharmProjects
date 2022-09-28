f=open("news","r")
lst=[]
data=0
dic={}
for i in f:
    print(i)
    data=i.rstrip("\n").split(' ')
    print(data)
    for i in data:
        print(i)
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
# for i in dic:
#     print(i,",",dic[i])
    #or
for k,v in dic.items():
    print(k,",",v)