import re
def is_valid_username(username):
    if len(username) >= 6 or len(username) >= 30: # Độ dài chuỗi từ 6 đến 30
        return True
    if re.match("^[a-zA-Z0-9]*$", username):#Các kí tự cho phép có thể là a-z hoặc A-Z hoặc 0-9 hoặc dấu chấm
        return True
    if username[0] != "." or username[-1] != ".": # Dấu chấm ko được phép ở đầu hoặc cuối chuỗi
        return True
    return False


def is_valid_password(password):
    if len(password) >= 12:#Ít nhất phải có 12 kí tự 
        return True
    if re.search("[a-z]", password): #Phải có cả kí tự chữ hoa và và chữ thường
        return True
    if re.search("[A-Z]", password):
        return True
    if re.search("0-9", password):#Phải có ít nhất 1 kí tự số 
        return True
    if re.search("[^a-zA-Z0-9]", password):# Phải có ít nhất 1 kí tự đặc biệt (các kí tự ko phải chữ và số đều được coi là kí tự đặc biệt. Ví dụ: @ ! # ...)
        return True
    return False


username, password = input("UserName:"), input("Password:")

if is_valid_username(username):
    print("User Vailed")
else:
    print("User Not vailed")

if is_valid_password(password):
    print("Password Vailed")
else:
    print("Password Not Vailed")
