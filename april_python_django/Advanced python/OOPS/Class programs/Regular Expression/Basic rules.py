#Basic rules
import re
count=0
rule='[abc]'#'[data]' - find the strings by each character
#'[^A-Z]' - will read the things except the string given
matcher=re.finditer(rule,'vishnu@abthebgjbdbchcbwfdnabc')

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)