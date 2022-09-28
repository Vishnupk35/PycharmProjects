#list slicing

#Print values from list based on index

lst=[15,20,25,30,35,40,45,50,55,60]
print(lst[1:4]) #lower limit=1, upper limit=4
print(lst[:7]) #Lower limit=0, upper limit=7
print(lst[3:]) #lowwr limit=3, upper limit= end
#Result: [20, 25, 30]
print(lst[:]) #print complete list

#Negative Index
#[-1 to -n]
print(lst[-1])#60 is the first index value from end
print(lst[-3])# 3rd element from the list end.
print(lst[-4:-1])# 4th element from end to 2nd element
print(lst[-2:-5]) #Not possible because it will print in reverse order for negative index
print(lst[-3:]) #-3,-2,-1
print(lst[:-4]) #print from 1st element -4th element