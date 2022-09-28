employee=['Vinay','Anu']
default={'Designation':'Bigdata','Salary':1000}

#print - Vinay's and anu's designation and salary
#fromkeys: It return a dictionary with specified keys and values

res=dict.fromkeys(employee,default)
print(res)
