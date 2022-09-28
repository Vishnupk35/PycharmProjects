#name, age, prof, salary
#name== fname
#prof
#company is present or not
#If not add new company=luminar
#Salary+5000
#print key value pairs

dic={"name":'Vishnu',"age":24,"proff":'Python',"Salary":1000}
print("proff" in dic)
if "company" not in dic:
    dic["company"]='Luminar'
dic["Salary"]=+5000
for i in dic:
    print(i,dic[i])
print(dic)