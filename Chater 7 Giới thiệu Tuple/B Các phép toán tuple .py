# Các phép toán thay đổi (KO dùng được):
# - Gán qua Access operator
# - Gán Quá trình tránh động
# - Gán qua phép gán (Assignment operator)
# -Gán qua Slicing
# appendnon>
# insert

x = (1, "Vu nguyen", 1.65, 65, [90, 60, 90])
# x[0] = 10
#x[4][0], x[4][1], x[4][2] = 4, 5, 6
#y = tuple(x)
y =tuple(item for item in x if type(item) == int)
print(y)
