#set operation

#1. Union
#2. Intersection
#3. Difference


#Union

#Elements of both combine and it will not create duplicates
st1={1,2,3,5,6,8,4,9,10}
st2={4,9,10,30,2,24,20,34,45,21,23}
# st3=st1.union(st2)
# print(st3)
#Result: {1, 2, 3, 4, 5, 6, 8, 9, 10, 20, 21, 23, 24, 30, 34, 45}


#Intersection
#Collect common elements from both sets.

# st3=st1.intersection(st2)
# print(st3)

#Difference
#A-B  Element should present in set A but not in set B 
st3=st1.difference(st2)
print(st3)
st4=st2.difference(st1)
print(st4)