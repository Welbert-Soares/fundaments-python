

class Animal:
  def __init__(self, nome: str) -> None:
    self.nome = nome

  def emitir_som(self):
    pass
  
  def andar(self):
    return f"{self.nome} está andando."
  
class Cachorro(Animal):
  def emitir_som(self):
    return "Au Au"
  
class Gato(Animal):
  def emitir_som(self):
    return "Miau"
  
dog = Cachorro(nome="Rex")

cat = Gato(nome="Mimi")

animais = [dog, cat]

for animal in animais:
  print(f"{animal.nome} faz {animal.emitir_som()}")
  print(animal.andar())

