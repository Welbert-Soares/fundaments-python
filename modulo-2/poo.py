

class Pessoa:
  def __init__(self, nome, idade) -> None:
    self.nome = nome
    self.idade = idade

  def apresentar(self):
    return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


lucas = Pessoa("Lucas", 20)
print(lucas.apresentar())

pedro = Pessoa(nome="Pedro", idade=25)
print(pedro.apresentar())