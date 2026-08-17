# Desafio 1: Ordenação de três números
'''
Recebidos 3 números inteiros, crie um programa que os mostre ordenados em ordem
crescente.
● Dica: Este desafio exige que você use estruturas if aninhadas ou uma série de testes
usando operadores de comparação para determinar qual número é o menor, o do
meio e o maior.
'''

print("==============================")
first_number = int(input("Insira o primeiro número: "))
second_number = int(input("Insira o segundo número: "))
third_number = int(input("Insira o terceiro número: "))

if first_number > second_number:
    first_number, second_number = second_number, first_number

if first_number > third_number:
    first_number, third_number = third_number, first_number

if second_number > third_number:
    second_number, third_number = third_number, second_number

print("------------------------------")
print(f"Ordem crescente: {first_number}, {second_number}, {third_number}")
print("==============================")