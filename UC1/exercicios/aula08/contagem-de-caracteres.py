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


def count_characters(text, desired_character):

    if len(desired_character) == 1:
        count = 0
        for character in text:
            if character == desired_character: 
                count += 1
        return count
    else:
        return -1


def separator(character):
    print(character * SEPARATOR_WIDTH)


separator("=")
print("Contador de caracteres".center(SEPARATOR_WIDTH))
separator("=")

text = input("Digite um texto: ")
text_lower = text.lower()
desired_character = input("Digite o caractere que deseja contar: ")
separator("-")
characters_count = count_characters(text_lower, desired_character)

if characters_count == -1:
    print("Entrada inválida: Insira apenas um caractere para realizar a contagem.")
    separator("=")
else:
    print(f"Foram encontradas {characters_count} ocorrências do caractere '{desired_character}' em: {text} ")
    separator("=")