'''
2. Contador de Frequência de Palavras
Crie uma função chamada contar_frequencia_palavras(texto).

Ela deve receber uma string (um parágrafo ou frase).
A função deve tratar todas as palavras como minúsculas (use .lower()) e pode usar .split() para separar o texto em uma lista de palavras.
Ela deve retornar um dicionário onde cada chave é uma palavra única e cada valor é o número de vezes que essa palavra apareceu no texto.
'''

  
def count_words_occurrence(text):
    split_text = text.lower().split(" ")

    result = {}
    for word in split_text:
        result[word] = split_text.count(word)

    return result


text = "o rato comeu o queijo do outro rato"

result = count_words_occurrence(text)
for key in result:
    print(f"{key} : {result[key]}")
