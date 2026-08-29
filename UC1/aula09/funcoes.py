
# SORTEIO DE NÚMEROS:
def sortear_numero(limite_inferior, limite_superior):
    '''
    Algoritmo escolhe e retorna um número inteiro aleatório no intervalo 
    passado através dos parâmetro.
    '''
    import random
    return random.randint(limite_inferior , limite_superior)

