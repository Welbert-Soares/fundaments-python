

def saudacao(nome):
    """
    Função que retorna uma saudação personalizada.
    
    Args:
        nome (str): O nome da pessoa a ser saudada.
    
    Returns:
        str: Mensagem de saudação.
    """
    return f"Olá, {nome}! Bem-vindo ao nosso módulo!"

def ImparOuPar(numero):
    """
    Função que verifica se um número é par ou ímpar.
    
    Args:
        numero (int): O número a ser verificado.
    
    Returns:
        str: Mensagem indicando se o número é par ou ímpar.
    """
    if numero % 2 == 0:
        return f"O número {numero} é par."
    else:
        return f"O número {numero} é ímpar."