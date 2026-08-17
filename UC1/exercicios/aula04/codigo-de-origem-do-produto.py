'''
4. Código de Origem do Produto:
Escreva um programa que leia o código de origem de um produto e imprima na tela a região
de sua procedência, conforme a tabela abaixo:

1 - Sul
2 - Norte
3 - Leste
4 - Oeste
5, 6 - Nordeste 
7, 8, 9 - Sudeste
10 - Centro-Oeste
11 - Noroeste

Observação: caso o código não seja nenhum dos especificados, o produto deve ser
encarado como “Importado”.
'''

code = int(input("Insira o código de origem do produto: "))

match code:
    case 1:
        origin = "Sul"
    case 2:
        origin = "Norte"
    case 3:
        origin = "Leste"
    case 4:
        origin = "Oeste"
    case 5 | 6:
        origin = "Nordeste"
    case 7 | 8 | 9:
        origin = "Sudeste"
    case 10:
        origin = "Centro-Oeste"
    case 11:
        origin = "Noroeste"
    case _:
        origin = "Importado"

print(f"Região de origem: {origin}.")