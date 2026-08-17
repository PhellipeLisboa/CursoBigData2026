'''
3. Rendimento do Taxista:
Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
média do consumo em km/L e o lucro (líquido) do dia.
'''

try:
    FUEL_PRICE = 6.15

    print("===================================================================================================")
    initial_odometer_reading = float(input("Insira a marcação do odômetro no início do dia em km: "))
    final_odometer_reading = float(input("Insira a marcação do odômetro no final do dia em km: "))
    fuel_consumed = float(input("Insira a quantidade de combustível gasta em litros: "))
    daily_ravenue = float(input("Insira o ganho total do dia: "))
    print("===================================================================================================")

    if fuel_consumed <= 0 or daily_ravenue <= 0:
        raise ValueError("Insira apenas valores numéricos e maiores que zero.")

    if initial_odometer_reading > final_odometer_reading:
        raise ValueError("O valor do marcador no final do dia deve ser maior que o valor no início do dia.")

    average_fuel_consumption = (final_odometer_reading - initial_odometer_reading) / fuel_consumed
    profit = daily_ravenue - (FUEL_PRICE * fuel_consumed)

    print(f"Consumo médio em km/L: {average_fuel_consumption:.2f}")
    print(f"Lucro do dia: R$ {profit:.2f}")
    print("===================================================================================================")
except ValueError as error:
    print(f"Entrada inválida: {error}")
    print("===================================================================================================")