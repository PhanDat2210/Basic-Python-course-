#Biểu diễn miền giá trị của biến x dưới dạng các mệnh đề logic theo các trường hợp trong hình vẽ.
#Biết các kí hiệu trên trục số được diễn giải như sau:
#a. [a,b] tức là x >= a và x <= b
#b. (a,b) tức là x >a và x < b
#c. |a tức là x == a
# \\\\\\ tức là ko lấy giá trị của đoạn đó

#a = float(input("Enter a :"))
#b = float(input("Enter b :"))

x = float(input("Enter x :"))

#print( x >= a and x <= b)

#print( x > a or x < b)

#print( x == a)

#print(x != a and x != b)

# (1) x ∈ [0,2)
print ("return value 1: ",0 <= x )

# (2) x ∈ [-1,2] ∪ [4,6]
print ("return value 2:", -1 <= x and x <= 2 or 4 <= x and x <= 6)

# (3) x ∈ (-2,2) x=5
print ("return value 3:", -2 <= x and x<=2 and x==5)

# (4) x ∈ (-4,0] ∪ (4,+∞)
print ("return value 4:",-4 < x and x <=0 or 4<x)