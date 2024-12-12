x = {"a": 1, "b": 2, "c": 3}
# number , bool ,str ,tule
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    1: "abc",
    True: "cdf",
    (2, 3): 100,
}
p1 ,p2,p3,p4,p5 = list(person.values())
print(p1, p2, p3, p4, p5)
print(person["name"])
print("age" in person)

print({element for element in person})
print({person[key] : key for key in person})
print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))#
