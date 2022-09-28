f=open("C:/Users/v-kvis/Downloads/temper","r")
dic={}
for i in f:
    data = i.rstrip("\n").split(",")
    dis = data[0]
    temp = data[1]

    if dis not in dic:
        dic[dis]=temp
    else:
        old=dic[dis]
        if temp>old:
            dic[dis]=temp
print(dic)

