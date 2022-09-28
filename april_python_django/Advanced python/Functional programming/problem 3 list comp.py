dic={"sedan":1500, "suv":2000, "pickup":2500, "minivan":1600,"van":2400,"semi":13600,"bicycle":1000}
#weight above 2000
# print vehicle name in upper case.
lst=[i.upper() for i in dic if dic[i]>2000]
print(lst)