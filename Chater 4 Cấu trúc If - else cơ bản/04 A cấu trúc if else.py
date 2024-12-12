tuoi = int (input("Nhap tuoi :"))
gioi_tinh = True # True la nam ,False la nu
#0....16...18...20

if tuoi >= 18 :
  print("Du tuoi di tu")
  print("So nam tu la 10 nam")
  if gioi_tinh:
     print("So nam tu la 10 nam")
  else :
     print("So nam tu la 11 nam")
elif 16<=tuoi <18:
    print("Vao trai cai tao")
else : 
    print("Chua du tuoi di tu")