'''
Exercício 8: classificação de valores

Nível: Básico

Conceitos praticados
- entrada de dados dentro de um while;
- variável de controle;
- múltiplos contadores;
- combinação de while com if/elif/else;
- classificação de valores;
- verificação dos resultados após o laço.

Enunciado: Escreva um programa que solicite ao usuário dez números. Durante a repetição, o programa deverá classificar cada número como:

- positivo;
- negativo;
- zero.

Ao final, exiba:

Quantidade de números positivos: resultado
Quantidade de números negativos: resultado
Quantidade de zeros: resultado

Exemplo de interação
Digite o 1º número: 8
Digite o 2º número: -4
Digite o 3º número: 0
Digite o 4º número: 3
...

Exemplo de resultado:
Quantidade de números positivos: 5
Quantidade de números negativos: 3
Quantidade de zeros: 2

Esses resultados são apenas ilustrativos e dependem das entradas fornecidas.

Restrições
Utilize while para controlar a quantidade de entradas.
Não utilize listas.
Não é necessário tratar entradas não numéricas neste momento.
Não armazene os dez números depois de classificá-los.
Não utilize três estruturas if independentes se apenas uma classificação pode ser verdadeira.
'''

positive_count = 0
negative_count = 0
zero_count = 0
count = 0

while count < 10:
    number = float(input(f"Digite o {count + 1}º número: "))
    if number < 0:
        negative_count += 1
    elif number > 0:
        positive_count += 1
    else:
        zero_count += 1
    count += 1

print(f"Quantidade de números positivos: {positive_count}")
print(f"Quantidade de números negativos: {negative_count}")
print(f"Quantidade de zeros: {zero_count}")