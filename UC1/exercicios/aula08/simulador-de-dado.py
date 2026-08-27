'''
3. Simulador de Dado
Usando o módulo random, crie uma função rolar_dado(lados).
● A função deve receber o número de lados do dado (ex: 6, 10, 20).
● Ela deve retornar um número aleatório entre 1 e o número de lados (use
random.randint(1, lados)).
● No programa principal, crie um "simulador de batalha":
○ Peça ao usuário para "Rolar para o Ataque (d20)". Chame a função
rolar_dado(20).
○ Peça ao usuário para "Rolar para o Dano (d8)". Chame a função
rolar_dado(8).
○ Imprima os resultados de cada rolagem
'''

import random

SEPARATOR_WIDTH = 60


def roll_dice(faces):
    return random.randint(1, faces)


def separator(character):
    print(character * SEPARATOR_WIDTH)


separator("=")
print("Simulador de batalha".center(SEPARATOR_WIDTH))
separator("=")
print("Escolha uma ação:")
print("1 - Atacar (d20)\n2 - Fugir(d10)")

try:
    option = int(input("Ação: "))
    separator("=")

    match option:
        case 1:
            d20 = roll_dice(20)
            print("Rolando um d20...")
            print(f"Você optou por atacar e tirou {d20} no d20.")
            separator('-')
            d8 = roll_dice(8)
            print("Rolando um d8 para verificar seu dano...")
            print(f"Seu dano foi {d8}.")
        case 2:
            d10 = roll_dice(10)
            print("Rolando um d10...")
            print(f"Você optou por fugir e tirou {d10} no d10.")
            separator('-')
        case _:
            print("Opção inválida!")
except ValueError:
    print("Entrada inválida: Insira apenas valores numéricos inteiros!")

separator('=')