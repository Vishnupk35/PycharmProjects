lst=[1,3,8,4,7,9,2,10,11]
search=5
#1. 1st step is sorting in Ascending order
lst.sort()
print(lst)

#2.Declare 2 variables
low=0
upp=len(lst)-1

#3. Calculate mid
mid=low+upp//2

#4. Conditions

#1. search_element>lst[mid]
#low=mid+1
#2. search_element<lst[mid]
#upp=mid-1
#3. search_element==lst[mid]

if (search>lst[mid]):
    low=mid+1
elif(search<lst[mid]):
    upp=mid-1
elif(search==lst[mid]):
    print("Search element found")


