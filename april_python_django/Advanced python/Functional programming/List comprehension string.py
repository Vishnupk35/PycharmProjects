# If string is vowel then print the vowel

name='luminartechnolab'
vowels='aeiou'
# lst=[i for i in name if i in vowels]
# print(lst)

## If string is vowel then print y else n
lst=['y' if i in vowels else 'n' for i in name]
print(lst)

