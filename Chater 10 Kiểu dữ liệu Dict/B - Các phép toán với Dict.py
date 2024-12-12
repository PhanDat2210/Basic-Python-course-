person = {"name": "Vu Nguyen", "age": 30, "city": "HCM"}
person["Address"] = "Ha Noi"
person["age"] += 1
person.update({"phone": "0123456789"})
person.pop("name")
#person.clear()
del person
for key in person:
    print(key, ": ", person[key])
