#tuples
#1. How to define
tu=()
print(type(tu))
#or
tu1=tuple()
print(type(tu1))
#2.Supports heterogenous data
tu2=(1,2.4,'bigdata',1,True)
print(tu2)
#3.Allows duplicates values.
#4. Insertion order is preserved.
#5. Tuple is immutable
tu2[1]=2
print(tu2)

#Difference between tuple and list.
#Tuple is immutable