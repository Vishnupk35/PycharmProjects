#1-50
#Print square if number is even else print the number itself.
lst=[(i,i**2) if i%2==0 else (i,i) for i in range(1,51)]
print(lst)