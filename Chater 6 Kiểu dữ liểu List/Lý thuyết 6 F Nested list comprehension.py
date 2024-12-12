#Lý thuyết 06.F.2 [*][optional] - Nested list comprehension : lồng nhau giữa các cấu trúc comprehension


x= [[1 , 2 ,3],['a','b','c'],[True, False]]
for sublist in x:
    for item in sublist:
        print(type(item))
type_x = [str(type(sublist).__name__)+ "_" + str(type(item).__name__) for sublist in x for item in sublist]
print(type_x)