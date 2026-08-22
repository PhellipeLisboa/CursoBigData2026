# Aula 05 - Dia 19/08/2026
# Tema principal: Estruturas de Repetição

# meunome = "Phellipe"

# for i in meunome:
#     print(i)

# for i in range(100, 10, -2):
#     print(i)

# WHILE

# somador = int(input("Registro: "))
# controle = 0

# while controle <= 30:
#     controle += somador 
#     somador = int(input("Registro: "))

# print("Oficina lotada!")


# for i in range(5):
#     try:
#         print(f"Número {i + 1} de 5:")
#         num = float(input("Digite um número: "))
#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4
#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")
#         num = float(input("Digite um número: "))

# contador = 0

# while contador < 5:
#     try:
#         print(f"Número {contador + 1} de 5:")
#         num = float(input("Digite um número: "))
#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4
#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
#         contador += 1
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")

print("--- Usando WHILE (Repetição Condicional) ---")
contador = 0 
limite = 5 

while True: 

    if contador >= limite:
        break

    try:
        print(f"Número {contador + 1} de {limite}:")
        num = float(input("Digite um número: "))
        dobro = num * 2
        triplo = num * 3
        quádruplo = num * 4
        print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
        contador += 1 
    except ValueError:
        print("Entrada inválida. Tente novamente.")