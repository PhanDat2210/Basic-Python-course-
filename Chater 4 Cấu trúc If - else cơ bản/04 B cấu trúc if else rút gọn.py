tuoi =16
#tuoi >=18
#ket_luan = "Du tuoi di tu" if tuoi >=18 else " Chua du tuoi di tu" 
#biểu thức dúng viết ở trước biểu thức sai viết ở sau
ket_luan = ("Chua du tuoi di du ","du tuoi di tu")[tuoi >=18]
# ngược lại       0                        1
print(ket_luan)