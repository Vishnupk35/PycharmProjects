lst=[[101,'Vishnu','pk',27,'python',1000],
    [102,'Prajith','kp',19,'bigdata',1500],
    [103,'Athul','krishna',21,'bigdata',1200],
    [104,'Abhi','jith',26,'c',1800]]

sum=0
#print id,fname,lname,age,profession
for i in lst:
    # print(i[0],i[1],i[2],i[3],i[4])
    # #or
    # print(i[0:5])
#age above 25 fname,lname,age,prof,salary
    # if (i[3]>25):
    #     print(i[1:6])
#working in big data (fname, lname, age, salary)
    # if(i[4]=='bigdata'):
    #     print(i[1:4],i[5])
#salary above 1750 and age above 25 (fname,lname,age,prof,salary)
    # if(i[3]>25):
    #     if(i[5]>1750):
    #         print(i[1],i[2],i[3],i[4],i[5])
#total salary
    sum+=i[5]
print(sum)



