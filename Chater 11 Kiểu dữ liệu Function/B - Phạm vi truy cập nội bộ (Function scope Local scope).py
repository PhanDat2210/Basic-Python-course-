# Lý thuyết 11.A - Kiểu dữ liệu Function
person = {
    "Name": "Vu",
    "weight": 65,
    "height": 1.65,
}
x = 1  # global scope


def show_heatlh():
    global person
    x =10
    result = ""  # function scope / local scope
    bmi = person["weight"] / person["height"] ** 2
    if bmi < 18.5:
        result = "Thiếu cân"
    elif 18.5 <= bmi < 24.9:
        result = "Bình thường"
    else:
        result = "Thừa cân"
    print(bmi, result)
    person = {"Name": "Vu Nguyen"}
    print('x inside func:,x')

show_heatlh()
print(person)
print('x outside func:',x)
