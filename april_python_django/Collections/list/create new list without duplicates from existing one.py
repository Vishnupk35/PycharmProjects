lst=[10,10,20,20,30,30,40,50,60,50,60,100,80,80,90]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)
