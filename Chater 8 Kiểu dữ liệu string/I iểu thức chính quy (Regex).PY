#Biểu thức cho phép tìm kiếm trong string theo các mẫu.
import re
s = 'abcde acbde abbde acccde axyze a123e a@!#e'

#pattern = 'a....e' # meta character
pattern = 'a[\w]{2,3}e' # meta character
#giải thích sau: \w: kiểu chữa ca đa cách, \d: kiểu chữa số, \s: kiểu chữa khoảng trảng, \D: kiểu chữa số, \S: kiểu chữa khoảng trảng

# . [] * + ? {n} {n,} {n,m} \ | ^ $ ( ) { } [ ] \d \D \w \W \s \S \b \B 

#pattern = 'a.*e' # meta character

# . [] * + ? {n} {n,} {n,m} \ | ^ $ ( ) { } [ ] \d \D \w \W \s \S \b \B

print(re.findall(pattern,s))
print(re.split(pattern,s))
#print(s.find('acbde'))#Tim xau trong xau

