class Phone:
    def __init__(self, country_code, state_code, incremental_code, phone_number):
        self.country_code = country_code
        self.state_code = state_code
        self.incremental_code = incremental_code
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.country_code} {self.state_code} {self.incremental_code} {self.phone_number}"


name = "Welbert Soares"


# interpolation
print(f"Hello, {name}!")


# concatenation
print("Hello, " + name + "!")

print("Hello, {}!".format(name))

print(name.strip("x"))

print(name.startswith("W"))


phone = "+55 (031) 9 95650333"
convert = phone.replace("+", "").replace("(", "").replace(")", "").replace("-", "")

phone_list = convert.split(" ")
print(phone_list)

phone = Phone(
    country_code=phone_list[0],
    state_code=phone_list[1],
    incremental_code=phone_list[2],
    phone_number=phone_list[3],
)
print(phone)


print("031" in phone.state_code)
print(type(phone.state_code))
