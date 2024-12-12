data = open('Chater Đọc nội dung file\info.txt', encoding='utf-8')

#print(data.readline())
#print(data.readline())
#for line in data:
  #  print(line)
#data.close()

print([line for line in data])
#file là 1 kiểu dữ liệu thuộc nhóm iterable