


my_list = [1, 2, 3, 4, 5, "hello", True, 3.14]
print("minha lista => ",my_list)

print("tamanho da lista => ", len(my_list))

my_list.append("mundo")
print("minha lista => ",my_list)

my_list.insert(2, "oi")

print("minha lista => ",my_list)

element_pop = my_list.pop(2)
print("ELEMENT POP => ",element_pop)

my_list.remove(3.14)
print("minha lista => ",my_list)

my_list.sort()
print("minha lista => ",my_list)