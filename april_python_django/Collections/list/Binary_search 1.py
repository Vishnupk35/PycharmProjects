lst=[1,5,2,7,3,8,4,9,10,23,12,46,22]
lst.sort()
search=int(input("Please enter the element to search: "))
low=0
upp=len(lst)-1
flg=0
while(low<=upp):
    mid=(low+upp)//2
    if(search>lst[mid]):
        low=mid+1
    elif(search<lst[mid]):
        upp=mid-1
    elif(search==lst[mid]):
        flg=1
        break
if(flg>0):
    print("Search element found")
else:
    print("Element not found")