# Aula 04 - Dia 19/08/2026
# Tema principal: Estruturas de Decisão II

# nome = input("Informe seu nome: ")
# if nome == "Pyetro":
#     resposta = "Pyetro presente!"
# elif nome == "Phellipe":
#     resposta = "Phellipe presente!"

mes = int(input("Informe o mês de seu nascimnto: "))

# Visão if/elif/else
# if mes == 1:
#     resultado = "Aquário"
# elif mes == 2:
#     resultado = "Peixes" 
# elif mes == 3:
#     resultado = "Áries" 
# elif mes == 4:
#     resultado = "Touro" 
# elif mes == 5:
#     resultado = "Gêmeos" 
# elif mes == 6:
#     resultado = "Câncer" 
# elif mes == 7:
#     resultado = "Leão" 
# elif mes == 8:
#     resultado = "Virgem" 
# elif mes == 9:
#     resultado = "Libra" 
# elif mes == 10:
#     resultado = "Escorpião" 
# elif mes == 11:
#     resultado = "Sagitário" 
# else:
#     resultado = "Capricórnio" 

# Visão match case

match mes:
    case 1:
        resultado = "Aquário"
    case 2:
        resultado = "Peixes"
    case 3:
        resultado = "Áries"
    case 4:
        resultado = "Touro"
    case 5:
        resultado = "Gêmeos"
    case 6:
        resultado = "Câncer"
    case 7:
        resultado = "Leão"
    case 8:
        resultado = "Virgem"
    case 9:
        resultado = "Libra"
    case 10:
        resultado = "Escorpião"
    case 11:
        resultado = "Sagitário"
    case 12:
        resultado = "Capricórnio"
    case _:
        resultado = "Mês inválido"

print(f"{resultado}.")