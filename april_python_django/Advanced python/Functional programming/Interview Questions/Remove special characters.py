data=open("Content","r")
string=""
sp='@#!$%^&'
for i in data:
    # print(i)
    data1=i.rstrip("\n")
    # print(data1)
    for i in data1:
        # print(i)
        if i not in sp:
            string+=i
print(string)



