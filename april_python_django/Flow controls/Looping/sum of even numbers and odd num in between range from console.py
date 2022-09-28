# sum of even numbers and odd num in between range from console
i=int(input("Please enter the lower limit:")) #1
u=int(input("Please enter the upper limit:")) #20
SUMO=0
SUME=0
while(i<=u):
    if(i%2==0):
        SUME+=i
    else:
        SUMO+=i
    i+=1
print(SUME)
print(SUMO)
