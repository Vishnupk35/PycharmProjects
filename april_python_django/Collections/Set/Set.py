#1. How to define
st=set()
#or
st1={1,2,3,5}
st2={}# Dictionary empty curly bracket is dictionary
print(type(st))
print(type(st1))

#2. It supports hetrogenous data
#3. Insertion order is not preserved.
#4. Duplicates not allowed( True not printed because True's default value is 1)
#5. Set is mutable
st3={1,7,3,4.5,'bigdata',True}
print(st3)