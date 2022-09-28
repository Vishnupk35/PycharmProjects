lst=[1,2,3,4,5,6,7,8]
element=int(input("Please enter the element: "))
lst.sort()
low=0
upp=len(lst)-1
while(low<=upp):
    data=lst[low]+lst[upp]
    if(element==data):
        print("pairs are ",lst[low],'and',lst[upp])
    elif(element>data):
