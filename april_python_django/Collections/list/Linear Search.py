lst=[1,2,3,4,5,6,7,8,9,10]
search=int(input("Please enter the element to find: "))
flg=0
for i in lst:
    if(search==i):
        flg=1
        break
if flg>0:
    print("Element found")
else:
    print("Element not found")


    #Linear search
    # Draw back

    #Complexity