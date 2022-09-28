f=open("april_data","r")
g=open("newdata","w")
for i in f:
    print(i)
    g.write(i)
