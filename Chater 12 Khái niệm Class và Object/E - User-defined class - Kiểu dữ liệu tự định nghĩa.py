class person:
    def __init__(self, name, age):  # constructor method
        print("Hello")
        self.name = name
        self.age = age

    def hello(self,default = False):
        print("Xin chao", self.name)
        if default :
            print(" 11 Xin chao",self.name)

vu = person("Anh Vu ", 30)
yen = person("thi yen", 25)

print(vu.name, vu.age)
print(yen.name, yen.age)

vu.hello()

yen.hello(True)
