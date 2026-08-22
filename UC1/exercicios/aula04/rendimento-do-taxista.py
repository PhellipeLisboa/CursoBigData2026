'''
3. Rendimento do Taxista:
Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
média do consumo em km/L e o lucro (líquido) do dia.
'''

FUEL_PRICE = 6.15
SEPARATOR_WIDTH = 99

try:
    
    print("=" * SEPARATOR_WIDTH)
    initial_odometer_reading = float(input("Insira a marcação do odômetro no início do dia em km: "))
    final_odometer_reading = float(input("Insira a marcação do odômetro no final do dia em km: "))
    fuel_consumed = float(input("Insira a quantidade de combustível gasta em litros: "))
    daily_revenue = float(input("Insira o ganho total do dia: "))
    print("=" * SEPARATOR_WIDTH)
 
    errors = []

    if initial_odometer_reading < 0 or final_odometer_reading < 0:
        errors.append(
            "Entrada inválida: o valor do marcador não pode ser negativo."
        )
    
    if initial_odometer_reading >= final_odometer_reading:
        errors.append(
            "Entrada inválida: o valor do marcador no final do dia deve ser maior que o valor no início do dia."
        )

    if fuel_consumed <= 0:
        errors.append(
            "Entrada inválida: a quantidade de combustível consumida deve ser maior que zero."
        )
    
    if daily_revenue <= 0:
        errors.append(
            "Entrada inválida: o ganho total do dia deve ser maior que zero."
        )

    if not errors:
        average_fuel_efficiency = (final_odometer_reading - initial_odometer_reading) / fuel_consumed
        profit = daily_revenue - (FUEL_PRICE * fuel_consumed)

        print(f"Consumo médio em km/L: {average_fuel_efficiency:.2f}")
        print(f"Resultado líquido do dia: R$ {profit:.2f}")
        print("=" * SEPARATOR_WIDTH)
    else:
        for error in errors:
            print(error)
            print("-" * SEPARATOR_WIDTH)
except ValueError:
    print("=" * SEPARATOR_WIDTH)
    print("Entrada inválida: insira apenas valores numéricos.")
    print("=" * SEPARATOR_WIDTH)