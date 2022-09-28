lst=[5,6,7,8,9]
try:
    print(lst[5])
except:
    print("range greater than", len(lst)-1)
finally:
    print("thank you")
