'''
2. Contagem de Caracteres
Crie uma função chamada contar_caractere(texto, caractere_procurado):
● A função deve receber uma string texto e uma string caractere_procurado (de um só
caractere).
● Ela deve retornar o número de vezes que o caractere_procurado aparece no texto.
(Não diferencie maiúsculas de minúsculas!)
● Dica: Use um loop for para percorrer o texto e use .lower() para tratar os caracteres.
● No programa principal, peça ao usuário uma frase e uma letra, e mostre o resultado
da contagem.    
'''

SEPARATOR_WIDTH = 75


def count_character_occurrences(text, target_character):
    if len(target_character) != 1:
        return -1
        
    target_character = target_character.lower()
    count = 0

    for character in text.lower():
        if character == target_character: 
            count += 1

    return count


def print_separator(character):
    print(character * SEPARATOR_WIDTH)


print_separator("=")
print("Contador de caracteres".center(SEPARATOR_WIDTH))
print_separator("=")

text = input("Digite um texto: ")
desired_character = input("Digite o caractere que deseja contar: ")
print_separator("-")
character_occurrences = count_character_occurrences(text, desired_character)

if character_occurrences == -1:
    print("Entrada inválida: insira apenas um caractere para realizar a contagem.")
elif character_occurrences == 1:
    print(f"Foi encontrada {character_occurrences} ocorrência do caractere '{desired_character}' em: {text}")
else:
    print(f"Foram encontradas {character_occurrences} ocorrências do caractere '{desired_character}' em: {text}")

print_separator("=")