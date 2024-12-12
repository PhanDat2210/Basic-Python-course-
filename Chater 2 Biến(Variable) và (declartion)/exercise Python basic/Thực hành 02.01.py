#Cho các biến thông tin age, fullname, country, weight.
#In ra đoạn văn bản giới thiệu bản thân như trong ảnh minh họa.

#age =20
#fullname = "Maria Ozawa"
#country = "Japan"
#weight =45.5

#print("Xin chao.",end =' ')
#print(f"Toi la {fullname} \nToi den tu {country} \nNam nay toi {age} tuoi \nToi nang {weight} kg",end='\n\n')

#Nhập đoạn văn bản giới thiệu bản thân như trong ảnh minh họa.

age, fullname, country, weight = input("Information:").split(",")   #20,"Maria Ozawa","Japan",45.5

# Xóa dấu ngoặc kép nếu có
fullname = fullname.strip('"')
country = country.strip('"')

print(f"Xin chao. Toi la {fullname} \nToi den tu {country} \nNam nay toi {age} tuoi \nToi nang {weight} kg")
