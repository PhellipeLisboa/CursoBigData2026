'''
1. Cálculo de Lâmpadas: 
Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para 
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da 
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do 
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada 
3m² existe um bocal para uma lâmpada.
'''

import math

try: 
    print("=====================================================================")
    lamp_wattage = int(input("Digite a potência da lâmpada em Watts: "))
    room_width = float(input("Digite a largura do cômodo em metros: "))
    room_length = float(input("Digite o comprimento do cômodo em metros: "))

    if lamp_wattage <= 0 or room_width <= 0 or room_length <= 0:
        raise ValueError

    room_area = room_length * room_width
    available_lamp_slots = math.ceil(room_area / 3)

    required_wattage = 3 * room_area

    min_lamp_wattage = math.ceil(required_wattage / available_lamp_slots)

    required_lamps = math.ceil(required_wattage / lamp_wattage)

    print("=====================================================================")
    print(f"A área do cômodo é de: {room_area} m²")
    print(f"O número de bocais disponíveis é: {available_lamp_slots}")
    print(f"A potêncial total necessária para iluminar este cômodo é de: {required_wattage} W")
    print("=====================================================================")
    
    if required_lamps < available_lamp_slots:
        print(f"Utilizando lâmpadas de {lamp_wattage} W, não será necessário utilizar todos os bocais disponíveis nesse cômodo. O número de lâmpadas necessárias será: {required_lamps} lâmpadas.")
    elif required_lamps == available_lamp_slots:
        print(f"Utilizando lâmpadas de {lamp_wattage} W, todos os bocais disponíveis nesse cômodo deverão ser utilizados, ou seja, serão necessárias {required_lamps} lâmpadas.")
    else:
        print(f"Este cômodo não possui bocais suficientes para iluminar de forma adequada com lâmpadas de {lamp_wattage} W. Opte por lâmpadas de pelo menos {min_lamp_wattage} W")
    
    
except ValueError:
    print("=====================================================================")
    print("Insira apenas valores numéricos e maiores que zero.")
    

