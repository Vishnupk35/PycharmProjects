lst=[('vinay',45),('arjun',35),('amal',65),('vipin',56)]
marks=[]#Created empty list

for i in lst:
    marks.append(i[1])
maximum=max(marks)#max function to find the highest value in the list.
for j in lst:
    if j[1]==maximum:
        print(j[0])

