x = ['a','b','c']
y = [100,200,300] # y =[100+0, 200+1, 300+2]
for i in enumerate(x):
    index ,value = i
    print(index, value)

print([index1+value1 for index1,value1 in enumerate(y)])
print([y[i] for i in range(len(y))])
