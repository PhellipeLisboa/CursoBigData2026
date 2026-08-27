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


def print_separator(character):
    print(character * SEPARATOR_WIDTH)


print_separator("=")
print("SIMULADOR DE BATALHA".center(SEPARATOR_WIDTH))
print_separator("=")

input("Pressione Enter para rolar o ataque (d20)...")
attack_roll = roll_dice(20)
print(f"Resultado da rolagem de ataque: {attack_roll}")

print_separator("-")

input("Pressione Enter para rolar o dano (d8)...")
damage_roll = roll_dice(8)
print(f"Resultado da rolagem de dano: {damage_roll}")

print_separator("=")
