'''
1. Cálculo de Lâmpadas: 
Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para 
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da 
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do 
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada 
3m² existe um bocal para uma lâmpada.
'''

WATTS_PER_SQUARE_METER = 3
SQUARE_METERS_PER_LAMP_SLOT = 3

try: 
    print("=====================================================================")
    lamp_wattage = int(input("Digite a potência da lâmpada em watts: "))
    room_width = float(input("Digite a largura do cômodo em metros: "))
    room_length = float(input("Digite o comprimento do cômodo em metros: "))

    if lamp_wattage <= 0 or room_width <= 0 or room_length <= 0:
        raise ValueError

    room_area = room_length * room_width
    required_wattage = WATTS_PER_SQUARE_METER * room_area
    required_lamps = int(required_wattage / lamp_wattage)

    if (required_lamps * lamp_wattage) < required_wattage:
        required_lamps += 1

    if room_area < SQUARE_METERS_PER_LAMP_SLOT:
        available_lamp_slots = 1
    else:
        available_lamp_slots = int(room_area / SQUARE_METERS_PER_LAMP_SLOT)

    print("=====================================================================")
    print(f"A área do cômodo é de: {room_area:.2f} m²")
    print(f"O número de bocais disponíveis é: {available_lamp_slots}")
    print(f"A potência total necessária para iluminar este cômodo é de: {required_wattage:.2f} W")
    print(f"A quantidade de lâmpadas de {lamp_wattage} W necessário para iluminar o cômodo é: {required_lamps}")
    print("=====================================================================")
    
    if required_lamps < available_lamp_slots:
        print("Não será necessário utilizar todos os bocais disponíveis nesse cômodo.")
    elif required_lamps == available_lamp_slots:
        print("Todos os bocais disponíveis nesse cômodo deverão ser utilizados.")
    else:
        print(f"Este cômodo não possui bocais suficientes para iluminá-lo de forma adequada com lâmpadas de {lamp_wattage} W.")
    
    
except ValueError:
    print("=====================================================================")
    print("Insira apenas valores numéricos e maiores que zero.")
    

