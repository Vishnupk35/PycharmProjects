f=open("C:/Users/v-kvis/Downloads/customer","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(",")

    proff=data[4]

    # if (age>'50'):
    #     if(country=='india'):
    #         print(data[1:6])
    if proff not in dic:
        dic[proff]=1
    else:
        dic[proff]+=1
print(dic)

