

def ParOuImpar(number):
  try:
      number = int(number)
      if number % 2 == 0:
        print("O número é par.")
      else:
        print("O número é ímpar.")
    
  except ValueError as e:
    print("O valor informado não é um número inteiro.", e)
    return
  
ParOuImpar(0)