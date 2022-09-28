f=open("Numbers","r")
lst=[]
SUM=0
for i in f:
    lst.append(int(i.rstrip("\n")))
print(lst)
print(sum(lst))
