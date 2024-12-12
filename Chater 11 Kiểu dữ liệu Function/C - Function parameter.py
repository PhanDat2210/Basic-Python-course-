# Lý thuyết 11.A - Kiểu dữ liệu Function
person = {
    "Name": "Vu",
    "weight": 65,
    "height": 1.65,
}


def conclusion(bmi):
    if bmi < 18.5:
        result = "Thiếu cân"
    elif 18.5 <= bmi < 24.9:
        result = "Bình thường"
    else:
        result = "Thừa cân"
    print(bmi, result)


def show_heatlh(weight, height, con):
    result = ""
    bmi = weight / height**2
    con(bmi)


show_heatlh(person["weight"], person["height"], conclusion)  # đôi số argument
show_heatlh(height=1.70, weight=75, con = conclusion)
show_heatlh(40, 1.65, conclusion)
