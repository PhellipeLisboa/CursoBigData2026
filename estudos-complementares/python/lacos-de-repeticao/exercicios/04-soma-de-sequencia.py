'''
# Exercício 4: soma de uma sequência

Nível: Básico

Conceitos praticados:
- variável de controle;
- acumulador;
- incremento;
- operação realizada depois do laço.

Enunciado: Escreva um programa que utilize while para calcular a soma de todos os números inteiros de 1 até 100. Ao final, exiba:

A soma dos números de 1 até 100 é: resultado

O programa não precisa solicitar entradas ao usuário.
'''

total = 0
current_number = 1
last_number = 100

while current_number <= last_number:
    total += current_number
    current_number += 1

print(f"A soma dos números de 1 até 100 é: {total}")