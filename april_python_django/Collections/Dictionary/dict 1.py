dic={"roll":101,"name":'Vinay',"age":26,"dept":'bigdata',"marks":30}
#keys: roll, name, age, dept, marks
# Collect values from dictionary by it's corresponding key.
print(dic["marks"])

#How to update values in dictioanry
dic["marks"]=40
#or dic['marks']=+10
dic["name"]='Vishnu'
print(dic)

#How to add key & values in dictioanry
dic["Total"]=150

#How to delete key & values in dictioanry
del dic["Total"]

#in Dic
print("name" in dic)

#Output: True


#Output required
#roll,101
#name,Vishnu
#age,26
#dep,bigdata
#marks,40
for i in dic:
    print(i,dic[i])
