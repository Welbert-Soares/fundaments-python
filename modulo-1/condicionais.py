# if, elif e else

age = 12

if age >= 18:
    print("Maior de idade")
else: 
    print("Menor de idade")

if age >= 18:
    print("trabalho tradicional permitido")
elif age >= 16:
    print("trabalho tradicional permitido com restrições")
else:
    print("trabalho tradicional não permitido")

message = "Maior de idade" if age >= 18 else "Menor de idade"
print(message)