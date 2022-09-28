#1,30
#If number is even print the element and print even else print odd and element
lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,31)]
print(lst)