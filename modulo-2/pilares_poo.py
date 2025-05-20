
# Definição de polimorfismo e Herança
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

# Definição de encapsulamento

class ContaBancaria:
  def __init__(self, saldo: float) -> None:
    self.__saldo = saldo

  def depositar(self, valor: float):
    if valor > 0:
      self.__saldo += valor
    else:
      print("Depósito inválido.")

  def sacar(self, valor: float):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor
    else:
      print("Saque inválido.")

  def consultar_saldo(self):
    return self.__saldo


conta = ContaBancaria(saldo=1000.0)
print(f"Saldo inicial: {conta.consultar_saldo()}")

conta.depositar(valor=500.0)
print(f"Saldo após depósito: {conta.consultar_saldo()}")

conta.sacar(valor=200.0)
print(f"Saldo após saque: {conta.consultar_saldo()}")

conta.sacar(valor=2000.0)
print(f"Saldo após saque inválido: {conta.consultar_saldo()}")


# Definição de abstração

from abc import ABC, abstractmethod

class Veiculo(ABC):
  
  @abstractmethod
  def ligar(self):
    pass
  
  @abstractmethod
  def desligar(self):
    pass

class Carro(Veiculo):
  def __init__(self) -> None:
    pass

  def ligar(self):
    return "Carro ligado."
  
  def desligar(self):
    return "Carro desligado."

carro = Carro()
print(carro.ligar())
print(carro.desligar())