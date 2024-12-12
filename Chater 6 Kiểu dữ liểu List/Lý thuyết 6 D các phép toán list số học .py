#Lý thuyết 06.D - Các phép toán với list số học
#Khi các phần tử trong list có kiểu dữ liệu số học, ta có thể thực hiện các phép tính tổng,
#  max, min, trung bình cộng,... đối với list này
import statistics
x = [3,6,1.5,5,2,-1]
x.sort() # sap xep tang dan
x.sort(reverse=True) # sap xep giam dan
print(sum (x))
print(max(x))
print(min(x))
print(statistics.mean(x))# giá trị trung bình

