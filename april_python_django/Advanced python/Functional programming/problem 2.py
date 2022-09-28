#even==> square
#5 divisible==> 0
#odd==> number

lst=[i**2 if i%2==0 else 0 if i%5==0 else i for i in range(1,51)]
print(lst)
