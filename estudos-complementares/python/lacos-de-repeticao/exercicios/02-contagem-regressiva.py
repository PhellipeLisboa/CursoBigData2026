'''
Exercício 2: contagem regressiva

Nível: Básico.

Enunciado: Escreva um programa que utilize while para imprimir os números de 10 até 1.

Depois que o laço terminar, exiba:

Contagem finalizada!

Ponto de atenção: A variável de controle deverá se aproximar do valor que torna a condição falsa. Nesse exercício, isso provavelmente ocorrerá por meio de um decremento.

'''

number = 10

while number >= 1:
    print(number)
    number -= 1

print("Contagem finalizada!")