'''
3. Elementos em Comum (Interseção)
Crie uma função chamada encontrar_elementos_comuns(lista1, lista2).

Ela deve receber duas listas.
A função deve retornar um set (conjunto) contendo apenas os elementos que existem em ambas as listas. (A conversão para set facilita muito isso).
'''


def find_intersection(list1, list2):

    first_set = set(list1)
    second_set = set(list2)

    return first_set.intersection(second_set)


list1 = [2, 6, 6, 5, 4, 7, 0]
list2 = [6, 5, 90, 2]
print(find_intersection(list1, list2))