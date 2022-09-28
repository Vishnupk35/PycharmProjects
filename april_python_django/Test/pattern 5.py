# 4. Print a pattern like
#
#        1
#        2 3
#        4 5 6
#        7 8 9 10
#        11 12 13 14 15

for i in range(1,16): #i=1, i=1
    for j in range(i,(i+1)):
        print(j,end=' ')
    print()