'''
2. Calculadora de IMC
Crie um programa que leia a altura e o peso de N pessoas (pergunte ao usuário quantas
pessoas são). Para cada pessoa, mostre seu IMC e a classificação.
● Fórmula: IMC = PESO / (ALTURA * ALTURA)
● Obrigatório (Função 1): Crie uma função calcular_imc(peso, altura) que receberá
os valores e retornará o IMC calculado.
● Obrigatório (Função 2): Crie outra função obter_classificacao(imc) que recebe o
valor do IMC (calculado pela função 1) e retorna uma string com a classificação.
○ Valores de Referência:
■ Menor que 18.5: "Abaixo do peso"
■ 18.5 a 24.9: "Peso normal"
■ 25.0 a 29.9: "Sobrepeso"
■ 30.0 ou mais: "Obesidade"
● O programa principal deve pedir N, fazer um loop N vezes, pedir peso e altura,
chamar as duas funções e imprimir o resultado formatado.
'''
SEPARATOR_WIDTH = 110


def print_separator(character):
    print(character * SEPARATOR_WIDTH)


def calculate_bmi(weight, height):
    return weight / (height * height)


def get_bmi_classification(bmi):
    if bmi < 18.5:
        return "Abaixo do peso"
    elif bmi < 25:
        return "Peso normal"
    elif bmi < 30:
        return "Sobrepeso"
    else: 
        return "Obesidade"


print_separator("=")
print("CALCULADORA DE IMC".center(SEPARATOR_WIDTH))
print_separator("=")
while True:
    try:
        people_count = int(input("De quantas pessoas deseja calcular o IMC? "))

        if people_count <= 0:
            print("Entrada inválida: digite apenas números inteiros e maiores que zero.")
            print_separator("-")
            continue

        break
    except ValueError:
        print("Entrada inválida: digite apenas valores numéricos.")
        print_separator("-")

for person_index in range(people_count):
    while True:
        try: 
            print_separator("-")
            weight = float(input(f"Digite o peso em kg da {person_index + 1}ª pessoa: ").replace(",", "."))
            height = float(input(f"Digite a altura em m da {person_index + 1}ª pessoa: ").replace(",", "."))
            print_separator("-")

            if weight <= 0 or height <= 0:
                print("Entrada inválida: o peso e a altura devem ser maiores que zero.")
                continue

            break
        except ValueError:
            print("Entrada inválida: digite apenas valores numéricos.")

    bmi = calculate_bmi(weight, height)
    classification = get_bmi_classification(bmi)
    print(f"O IMC da {person_index + 1}ª pessoa é {bmi:.2f}.")
    print(f"Classificação: {classification}")
print_separator("=")