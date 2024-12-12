# Lý thuyết 11.A - Kiểu dữ liệu Function
person = {
    "Name": "Vu",
    "weight": 65,
    "height": 1.65,
}


def show_heatlh(weight, height):
    if weight <= 0 or height <= 0:
        print("Can nhap lai")
        return
    result = ""
    bmi = weight / height**2
    if bmi < 18.5:
        result = "Thiếu cân"
    elif 18.5 <= bmi < 24.9:
        result = "Bình thường"
    else:
        result = "Thừa cân"
    # print(bmi,result)
    return bmi, result  # tra ve 1 doi tuong tuple


x, y = show_heatlh(65, 1.65)
if x != None:
    print(x, y)
