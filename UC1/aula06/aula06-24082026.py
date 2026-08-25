# Aula 06 - Dia 24/08/2026
# Tema principal: Estruturas de Dados

# LISTAS

# impares = []
# print(type(impares))
# impares = [3, 5, 13, 27]
# print(impares)
# print(impares[0])
# print(type(impares[0]))
# print(impares[-4])


#IndexError: list index out of range
# print(impares[-5])
# print(impares[15])]

# lista_01 = [
#     12,
#     "Pedro",
#     12.53343,
#     "{}{}^^",
#     False,
#     0,
#     [2,4,6,8]
#     ]

# print(lista_01[1])
# print(lista_01[2])
# print(lista_01[4])
# print(lista_01[6][2])

# lista_02 = ["Márcia"]
# # Operador in
# if "Márcia" in lista_02:
#     print(lista_02)
# else:
#     print("Márcia não está presente na lista.")

# LOOPINGS

# participantes = ["Isaque", "Luana", "Fernando", "Bianca", "Ana Paula"]

# for participante in participantes:
    # print(participante)

# partic_2 = "Hugo"
# participantes.append(partic_2)
# participantes.insert(2, partic_2)
#print(participantes)

# participantes.pop(1)
# participantes.remove("Hugo")
# participantes.reverse()
# participantes.count("Hugo")
# print(participantes.index("Bianca"))
# participantes.clear()


# print(participantes)


# teste = ["teste", "teste2"]
# print(participantes + teste)
# print(participantes)

# TUPLAS

participantes = ("Isaque", "Luana", "Fernando", "Bianca", "Ana Paula")

# print(participantes, type(participantes))
# partic_2 = ("Hugo")
# resultado = participantes + partic_2
# print(participantes.count("Luana"))
# print(resultado)

participante_02 = ("Fernando", "111.111.******", "Avenida Dr. Tiburcio, 444")
# print(participante_02.index("111.111.******"))

listinha_partic_02 = list(participante_02)
tupla_partic_02 = tuple(participante_02)
# print(listinha_partic_02)
# print(tupla_partic_02)


#SETS

numeros_pares = {
    202,
    203,
    204,
    204,
    205,
    219,
    291,
    292,
    202
}

numeros_impares = {111, 111, 112, 291, 291, 205}

# print(numeros_pares.intersection(numeros_impares))
# print(numeros_pares, type(numeros_pares))

numeros_pares.discard(291)
numeros_pares.discard(205)
# print(numeros_pares)

# Dicionarios

produtos = {
    "maçã": 5.99, 
    "laranja": 4.79 
}

# print(produtos, type(produtos))
# print(produtos.items())
# print(produtos.keys())
# print(produtos.values())
# print(produtos['laranja'])
# print(produtos.get('laranja'))
produtos2 = produtos.copy()
# print(produtos2)
# produtos2.pop("maçã")
produtos2["maçã"] = 7.99
print(produtos2)

achadinhos = {}
print(type(achadinhos))
achadinhos["capinha celular"] = 12.99

print(achadinhos)