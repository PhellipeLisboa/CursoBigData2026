'''
2. Quantidade de Caixas de Azulejos: 
Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, 
largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em 
todas as suas paredes (considere que não será descontada a área ocupada por portas e 
janelas). Cada caixa de azulejos possui 1,5 m² 
'''

AREA_COVERED_PER_BOX = 1.5
SEPARATOR_WIDTH = 85

try:
    print("=" * SEPARATOR_WIDTH)
    kitchen_width = float(input("Digite a largura da cozinha em metros: "))
    kitchen_length = float(input("Digite o comprimento da cozinha em metros: "))
    kitchen_height = float(input("Digite a altura da cozinha em metros: "))

    if kitchen_width <= 0 or kitchen_length <= 0 or kitchen_height <= 0:
        print("=" * SEPARATOR_WIDTH)
        print("Entrada inválida: insira apenas valores maiores que zero.")
        print("=" * SEPARATOR_WIDTH)
    else:
        walls_area = 2 * kitchen_height * (kitchen_width + kitchen_length)

        tile_box_count = int(walls_area / AREA_COVERED_PER_BOX)
        covered_area = tile_box_count * AREA_COVERED_PER_BOX

        if covered_area < walls_area:
            tile_box_count += 1
        
        print("=" * SEPARATOR_WIDTH)
        print(f"Área total das paredes: {walls_area:.2f} m²")
        print(f"A quantidade de caixas de azulejos necessária para preencher todas as paredes é: {tile_box_count}")
        print("=" * SEPARATOR_WIDTH)

except ValueError:
    print("=" * SEPARATOR_WIDTH)
    print("Entrada inválida: insira apenas valores numéricos.")
    print("=" * SEPARATOR_WIDTH)
        