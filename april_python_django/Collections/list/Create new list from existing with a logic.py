lst=[4,5,10,12,20]
lst1=[]
SUM=sum(lst)
print(SUM)
for i in lst:
    res=SUM-i
    lst1.append(res)
    print(lst1)

print(lst1)