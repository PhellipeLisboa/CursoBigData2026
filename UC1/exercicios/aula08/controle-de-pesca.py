'''
1. Controle de Pesca
Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
pagar uma multa de R$ 4,00 por quilo excedente.
● O programa deve ler o peso de peixes (em quilos) pescado no dia.
● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
● Se o valor da multa retornado for maior que zero, mostre a multa.
● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
pagar."
● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.
'''

SEPARATOR_WIDTH = 110
WEIGHT_LIMIT = 100
FINE_RATE_PER_KILOGRAM = 4


def calculate_fine(fish_weight):
    if fish_weight > WEIGHT_LIMIT:
        excess_weight = fish_weight - WEIGHT_LIMIT
        return FINE_RATE_PER_KILOGRAM * excess_weight
    return 0


def print_separator(character):
    print(character * SEPARATOR_WIDTH)


print_separator("=")
print("CONTROLE DE PESCA".center(SEPARATOR_WIDTH))
print_separator("=")

total_fine = 0
while True:
    try:
        fish_weight = float(input("Digite o peso total de peixe de sua pescaria em quilos (ou 0 para encerrar): ").replace(",", "."))

        print_separator("-")

        if fish_weight == 0:
            break

        if fish_weight < 0:
            print("Entrada inválida: o peso não pode ser negativo.")
            print_separator("-")
            continue

        fine = calculate_fine(fish_weight)
        if fine > 0:
            print(f"A multa aplicada para os {fish_weight - WEIGHT_LIMIT:.2f} kg acima do limite permitido de {WEIGHT_LIMIT} kg será de: R$ {fine:.2f}")

            print_separator("-")
        else:
            print("Peso dentro do limite. Nenhuma multa a pagar.")
            print_separator("-")

        total_fine += fine
    except ValueError:
        print_separator("-")
        print("Entrada inválida: digite apenas valores numéricos.")
        print_separator("-")

print(f"O total de multa acumulado é de: R$ {total_fine:.2f}")
print_separator("=")
