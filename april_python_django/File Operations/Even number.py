f=open("Numbers","r")
lst=[]
odd=[]
even=[]
for i in f:
    lst.append(int(i.rstrip("/n")))
print(lst)
for i in lst:
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(odd)
print(sum(odd))
print(even)
print(sum(even))