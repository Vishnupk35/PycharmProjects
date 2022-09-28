Line='cat rat bus cat car car rat bus car car bus cat'
#1. Lien of data needs to be converted to word by word data using split.
#split
data=Line.split(' ')
print(data)
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

print(dic)
