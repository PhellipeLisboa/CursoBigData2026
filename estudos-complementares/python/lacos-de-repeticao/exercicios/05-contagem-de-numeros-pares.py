'''
Exercício 5: contagem de números pares

Nível: Básico.

Conceitos praticados
- variável de controle;
- contador;
- combinação de while com if;
- operador de módulo %;
- separação de responsabilidades entre variáveis.

Enunciado: Escreva um programa que percorra todos os números inteiros de 1 até 50 utilizando while. Durante a repetição, conte quantos desses números são pares. Ao final, exiba:

Quantidade de números pares entre 1 e 50: resultado

O programa não precisa solicitar dados ao usuário.

Restrição: Não avance diretamente de dois em dois. Neste exercício, percorra todos os números entre 1 e 50 e utilize uma condição para identificar os pares.
'''

even_count = 0
current_number = 1
final_number = 50

while current_number <= final_number:
    if current_number % 2 == 0:
        even_count += 1
    current_number += 1

print(f"Quantidade de números pares entre 1 e {final_number}: {even_count}")