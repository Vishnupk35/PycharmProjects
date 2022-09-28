#Regular expression (re)
#It's a package
#It's used for pattern matching
#string is a pattern
#Regular expression is used for validation.
#Example: We provide mobile numbers in sites, normally it will be 10 digits but if we give 9 digts then it shows an error.
#example2: Special character required in password
# How to import the regular expression package (re) It's an inbuit package in python.
#import re #There are lot of functions in this package
#finditer(arg1,arg2) #finditer is used to find the required string is present or not/
#arg1=pattern to match or item to find
#arg2=string name

import re
s='abdbfbfbbfbfbfbfbfbbfbfbbfbfbabbbabababababdbfbbfbfbabbb'
count=0
#how many times ab present in the mentioned string
matcher=re.finditer('ab',s)
#print(matcher) #it will print the location only
for i in matcher:
    count+=1
    print(i.group())#i.group will show the string matched
    print(i.start())#i.start will show on which index the repective string found
print(count)