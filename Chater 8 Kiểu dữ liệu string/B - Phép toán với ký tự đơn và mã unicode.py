x = "Vu nguyen coder"
#print(ord("A"))
#print(chr(65)) #chr - character | ord - ordinal

for item in range(ord('a'),ord('z')):
    print(item,sep = ' ',end = ' ')
    
#list comprehension

[item for item in range(ord('a'),ord('z'))]