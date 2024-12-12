import math 
#1 - 
x = 2
y = x - 0.5
print (int(y) == x)  # 1 != 2 false
#2 
x = 0
x +=1 # x =  x + 1
b = x == 1 # b = x == 1
print(b) # in ra true
#3 - 
x = -1
y = x * x + abs(x) * 2 # -1 * -1 + 1 * 2 = 3
print( y % 2) # 3 %2 = 1 lấy phần nguyên
#4 - 
x = 1
y = 2
z = 3
t = 3 * (z + (x+y) * (y+z)) #  3 * (3 + (1+2) * (2+3))
print(1 - 2 * t ) # -107
#5 - 
x = 1
y = 2
z = 3
b = (x<y) or (x>z) and ((y<z) or (x<z)) # (1<2) or (1>3) and ((2<3) or (1<3))
print(b) # True
#6 - 
x = 1
y = x + 1
z = x + y + 1
print(int(z)) # 4
#7 - 
x = 1.5
y = int(x)
z = str(y)
w = "abc"
print(z + w) # 1abc
#8 - 
x = int(1.5)
y = float(x) # 1
print (str(y)) # 1.0