'''
3. Conversor de Temperatura
Crie um programa que permita ao usuário converter temperaturas entre Celsius e
Fahrenheit.
● Função 1: Crie uma função celsius_para_fahrenheit(temp_c) que recebe a
temperatura em Celsius e retorna o valor em Fahrenheit.
○ Fórmula: F = (C * 9/5) + 32
● Função 2: Crie uma função fahrenheit_para_celsius(temp_f) que recebe a
temperatura em Fahrenheit e retorna o valor em Celsius.
○ Fórmula: C = (F - 32) * 5/9
● O programa principal deve perguntar ao usuário qual conversão ele quer fazer (ex:
"1 para C->F" ou "2 para F->C"), pedir o valor, chamar a função correta e mostrar o
resultado.
Desafio: Criar uma única função que faça qualquer uma das conversões,
sempre perguntando ao usuário qual é desejada.
'''

print("Qual conversão você deseja fazer?\n1 - Celsius para Fahrenheit\n2 - Fahrenheit para Celsius")
option = input("Opção desejada: ")


