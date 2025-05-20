

class Animal:
  def __init__(self, nome: str):
    self.nome = nome

  def emitir_som(self):
    pass

class Mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} está amamentando."
  
class Ave(Animal):
  def voar(self):
    return f"{self.nome} está voando."
  
class Morcego(Mamifero, Ave):
  def emitir_som(self):
    return "Som ultrassônico."
  
morcego = Morcego(nome="Bat")
morcego.amamentar()
morcego.voar()
morcego.emitir_som()
print(f"{morcego.nome} faz {morcego.emitir_som()}")
print(morcego.amamentar())
print(morcego.voar())