#Nhập từ bàn phím 3 số thực x, y, z
#1 - Tìm số lớn nhất trong 3 số x, y, z
#2 - Tìm số bé nhất trong 3 số x, y, z
#3 - Kiểm tra xem cả 3 số có cùng dấu hay ko?
#4 - In ra các cặp số trái dấu nhau.

x = float(input("Nhập x: "))
y = float(input("Nhập y: "))
z = float(input("Nhập z: "))

#1 - Tìm số lớn nhất trong 3 số x, y, z

if x > y and  x > z :
    print ("Ket qua 1: So lon nhat",x)
elif y > x and y> z:
    print ("Ket qua 1: So lon nhat",y)
else :
    print ("Ket qua 1: So lon nhat",z)

#2 - Tìm số bé nhất trong 3 số x, y, z
if x < y and x < z :
    print ("Ket qua 2: So nho nhat",x)
elif y < x and y < z:
    print ("Ket qua 2: So nho nhat",y)
else :
    print ("Ket qua 2: So nho nhat",z)

#Ket qua 3: Ca 3 so cung dau
if (x>0 and y > 0 and z >0) or (x < 0 and y < 0 and z <0):
    print ("Ket qua 3: Ca 3 so cung dấu")
else :
    print ("Ket qua 3: Ca 3 so khong cung dấu")

#4 - In ra các cặp số trái dấu nhau
if x > 0 and y > 0 and z < 0 :
    print ("Ket qua 4 :(",x,z,"),(",y,z,")")
    print (f"Ket qua 4: ({x:.1f},{y:.1f},{z:.1f})")
    print ("Ket qua 4 : ({},{}),({},{})".format(x,z,y,z))
elif x > 0 and y < 0 and z < 0:
    print ("Ket qua 4 :(",x,z,"),(",x,y,")")
elif x > 0 and y < 0 and z > 0:
    print ("Ket qua 4 :(",x,y,"),(",y,z,")")
elif x < 0 and y < 0 and z > 0:
        print ("Ket qua 4 :(",y,z,"),(",x,z,")")
elif x < 0 and y > 0 and z > 0:
            print ("Ket qua 4 :(",x,y,"),(",x,z,")")
elif x < 0  and y > 0 and z < 0:
                print ("Ket qua 4 :(",x,y,"),(",y,z,")")
else :
      print ("Ket qua 4 : Ko co cap so nao trai dau")