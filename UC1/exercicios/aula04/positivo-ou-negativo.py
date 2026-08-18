'''
6. Positivo ou Negativo:
Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
valor zero como positivo.
'''
try:
    print("==========================================================")
    number = float(input("Digite um número: "))
    print("==========================================================")

    if number < 0:
        result = "negativo"
    else:
        result = "positivo"

    print(f"O número {number} é {result}.")
    print("==========================================================")

except ValueError:
    print("==========================================================")
    print("Entrada inválida: Digite apenas valores numéricos.")
    print("==========================================================")