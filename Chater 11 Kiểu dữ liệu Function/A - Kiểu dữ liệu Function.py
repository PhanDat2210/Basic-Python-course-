#Lý thuyết 11.A - Kiểu dữ liệu Function
person = {
    'Name' : 'Vu',
    'weight' : 65,
    'height':1.65,
 
}
def show_heatlh():
    result = ''
    bmi = person['weight'] / person['height' ] ** 2
    if bmi <18.5:
        result = 'Thiếu cân'
    elif 18.5 <= bmi < 24.9:
        result = 'Bình thường'
    else:
        result = 'Thừa cân'
    print(bmi,result)
print("year1: ",end="")
show_heatlh()

person['weight'] =70
print('year2: ',end="")
show_heatlh()

print(type(show_heatlh))