#lower to upper even numbers print
lower=int(input("please enter the lower limit number:"))
upper=int(input("please enter the upper limit number:"))
for i in range(lower,upper+1):
    if(i%2==0):
        print(i)