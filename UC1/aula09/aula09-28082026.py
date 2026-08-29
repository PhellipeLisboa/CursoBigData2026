# Aula 09 - Dia 28/08/2026
# Tema principal: Funções/Exceções/Bibliotecas

import time

def dar_boas_vindas():
    print("-" * 40)
    print("Bem-vindo ao nosso aplicativo! 😃".center(40))
    print("-" * 40)


def dar_boas_vindas_personalizado(nome_da_pessoa):
    print("-" * 40)
    print(f"Olá, {nome_da_pessoa}! Seja bem-vindo ao nosso aplicativo! 😃".center(40))
    print("-" * 40)


def somar(a, b):
    resultado = a + b
    return resultado


# print("Início do programa.")
# print("Por favor, aguarde...")
# time.sleep(2)
# dar_boas_vindas()
# print("Meio do programa.")
# dar_boas_vindas()

# dar_boas_vindas_personalizado("Maria")
# dar_boas_vindas_personalizado("João")

# soma1 = somar(5, 10)
# soma2 = somar(100, 50)

# print(f"O primeiro resultado é: {soma1}")
# print(f"O primeiro resultado é: {soma2}")
