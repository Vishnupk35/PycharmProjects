f=open("C:/Users/v-kvis/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    country=data[5]
    if country in data:
        dic[country]=1
    else:
        dic[country]+=1
print(dic)
