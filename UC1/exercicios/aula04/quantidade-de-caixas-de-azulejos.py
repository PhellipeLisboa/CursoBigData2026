'''
2. Quantidade de Caixas de Azulejos: 
Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, 
largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em 
todas as suas paredes (considere que não será descontada a área ocupada por portas e 
janelas). Cada caixa de azulejos possui 1,5 m² 
'''

import math

try:
    print("=====================================================================================")
    kitchen_width = float(input("Digite a largura da cozinha em metros: "))
    kitchen_length = float(input("Digite o comprimento da cozinha em metros: "))
    kitchen_height = float(input("Digite a altura da cozinha em metros: "))

    if kitchen_width <= 0 or kitchen_length <= 0 or kitchen_height <= 0:
        raise ValueError

    walls_area = 2 * kitchen_height * (kitchen_width + kitchen_length)

    AREA_COVERED_PER_BOX = 1.5
    tile_box_count = math.ceil(walls_area / AREA_COVERED_PER_BOX)

    print("=====================================================================================")
    print(f"A quantidade de caixas de azulejos necessária para preencher todas as paredes é: {tile_box_count}.")

except ValueError:
    print("=====================================================================================")
    print("Insira apenas valores numéricos e maiores que zero.")
        