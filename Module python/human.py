max_age = 100
bmi = lambda w, h : w/h ** 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
       print(f'Hello! I am {self.name}. I am {self.age} years old')
