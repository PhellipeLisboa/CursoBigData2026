'''
6. Positivo ou Negativo:
Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
valor zero como positivo.
'''

SEPARATOR_WIDTH = 58

try:
    print("=" * SEPARATOR_WIDTH)
    number = float(input("Digite um número: "))
    print("=" * SEPARATOR_WIDTH)

    if number < 0:
        result = "negativo"
    else:
        result = "positivo"

    print(f"O número {number} é {result}.")
    print("=" * SEPARATOR_WIDTH)

except ValueError:
    print("=" * SEPARATOR_WIDTH)
    print("Entrada inválida: digite apenas valores numéricos.")
    print("=" * SEPARATOR_WIDTH)