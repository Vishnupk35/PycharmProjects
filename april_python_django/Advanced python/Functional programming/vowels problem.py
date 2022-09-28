#read a string from string.
data=input("Enter the word")
string=""
vow='aeiouAEIOU'
for i in data:
    if i not in vow:
        string+=i
print(string)

