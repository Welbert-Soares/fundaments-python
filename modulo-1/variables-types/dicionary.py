

people = {"name": "John", "age": 30, "city": "New York"}
print(people)

print("Name => ", people["name"])

people["last_name"] = "Doe"
print("Last name => ", people["last_name"])
print("People => ", people)

del people["last_name"]
print("People => ", people)

# methods: keys(), values(), items()
print("Keys => ", people.keys())
print("Values => ", people.values())
print("Items => ", people.items())