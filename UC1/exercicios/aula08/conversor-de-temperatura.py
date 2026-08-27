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

#OBS: Cursei três períodos de bacharelado em Física, e os 3/8 de físico que existem em mim me obrigaram a adicionar as conversões com Kelvin, validar o zero absoluto e exibir as unidades corretas.

ABSOLUTE_ZERO_CELSIUS = -273.15
ABSOLUTE_ZERO_FAHRENHEIT = -459.67
ABSOLUTE_ZERO_KELVIN = 0

SEPARATOR_WIDTH = 110


def celsius_to_fahrenheit(temperature_c):
    return (temperature_c * 9 / 5) + 32


def fahrenheit_to_celsius(temperature_f):
    return (temperature_f - 32) * 5 / 9


def celsius_to_kelvin(temperature_c):
    return temperature_c + 273.15


def kelvin_to_celsius(temperature_k):
    return temperature_k - 273.15


def fahrenheit_to_kelvin(temperature_f):
    temperature_c = fahrenheit_to_celsius(temperature_f)
    return celsius_to_kelvin(temperature_c)


def kelvin_to_fahrenheit(temperature_k):
    temperature_c = kelvin_to_celsius(temperature_k)
    return celsius_to_fahrenheit(temperature_c)


def convert_temperature(temperature, source_unit, target_unit):
    match source_unit:
        case "C":
            if target_unit == "F":
                return celsius_to_fahrenheit(temperature)
            else:
                return celsius_to_kelvin(temperature)
        case "F":
            if target_unit == "C":
                return fahrenheit_to_celsius(temperature)
            else:
                return fahrenheit_to_kelvin(temperature)
        case "K":
            if target_unit == "C":
                return kelvin_to_celsius(temperature)
            else:
                return kelvin_to_fahrenheit(temperature)
        case _:
            return

def validate_temperature(temperature, source_unit):
    is_valid = True
    cause = ""

    match source_unit:
        case "C":
            if temperature < ABSOLUTE_ZERO_CELSIUS:
                is_valid = False
                cause = f"A menor temperatura possível em Celsius é {ABSOLUTE_ZERO_CELSIUS} °C."
        case "F":
            if temperature < ABSOLUTE_ZERO_FAHRENHEIT:
                is_valid = False
                cause = f"A menor temperatura possível em Fahrenheit é {ABSOLUTE_ZERO_FAHRENHEIT} °F."
        case "K":
            if temperature < ABSOLUTE_ZERO_KELVIN:
                is_valid = False
                cause = f"A menor temperatura possível em Kelvin é {ABSOLUTE_ZERO_KELVIN} K."

    return {
        "is_valid": is_valid,
        "cause": cause
    }

def print_separator(character):
    print(character * SEPARATOR_WIDTH)


def print_menu():
    print_separator("=")
    print("CONVERSOR DE TEMPERATURA".center(SEPARATOR_WIDTH))
    print_separator("=")

    print("Escolha uma das opções abaixo para realizar a conversão: ")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")
    print("5 - Fahrenheit para Kelvin")
    print("6 - Kelvin para Fahrenheit")
    print("0 - Encerrar")
    print_separator("-")

        
while True:
    print_menu()
    try:
        option = int(input("Opção desejada: "))

        if option < 0 or option > 6:
            print("Entrada inválida: digite uma das opções válidas.")
            continue

        match option:
            case 1:
                source_unit = "C"
                source_unit_text = "°C"
                target_unit = "F"
                target_unit_text = "°F"
            case 2:
                source_unit = "F"
                source_unit_text = "°F"
                target_unit = "C"
                target_unit_text = "°C"
            case 3:
                source_unit = "C"
                source_unit_text = "°C"
                target_unit = "K"
                target_unit_text = target_unit
            case 4:
                source_unit = "K"
                source_unit_text = source_unit
                target_unit = "C"
                target_unit_text = "°C"
            case 5:
                source_unit = "F"
                source_unit_text = "°F"
                target_unit = "K"
                target_unit_text = target_unit
            case 6:
                source_unit = "K"
                source_unit_text = source_unit
                target_unit = "F"
                target_unit_text = "°F"
            case 0:
                print("Encerrando programa...")
                print_separator("=")
                break

        try:
            temperature = float(input(f"Digite a temperatura em {source_unit_text}: ").replace(",", "."))
            validation_result = validate_temperature(temperature, source_unit)
    
            if validation_result["is_valid"]:
                converted_temperature = convert_temperature(temperature, source_unit, target_unit)
                print(f"Conversão: {temperature} {source_unit_text} = {converted_temperature:.2f} {target_unit_text}")
            else:
                print(f"Temperatura inválida: {validation_result['cause']}")
                continue
        except ValueError:
            print("Entrada inválida: digite apenas valores numéricos para a temperatura.")

    except ValueError:
        print("Entrada inválida: digite apenas valores dentro das opções válidas.")
    


