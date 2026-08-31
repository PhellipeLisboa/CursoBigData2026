'''
1. Filtro de Números Pares e Ímpares
Crie uma função chamada separar_pares_impares(lista_numeros).

Ela deve receber uma lista de números inteiros.
Dentro da função, crie duas novas listas: uma para os pares e outra para os ímpares.
Use um loop for para percorrer a lista_numeros.
A função deve retornar um dicionário com duas chaves, 'pares' e 'impares', contendo as respectivas listas.
'''


def split_even_and_odd(numbers):
    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return {
        "even_numbers" : even,
        "odd_numbers": odd
    }


numbers = [2, 3, 5, 7, 33, 42, 57, 90]
print(f"Números pares: {split_even_and_odd(numbers)["even_numbers"]}")
print(f"Números ímpares: {split_even_and_odd(numbers)["odd_numbers"]}")