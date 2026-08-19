'''
Exercício 6: soma dos números pares

Nível: Básico

Conceitos praticados
- variável de controle;
- acumulador;
- combinação de while com if;
- operador de módulo %;
- diferença entre contar ocorrências e acumular valores.

Enunciado: Escreva um programa que percorra todos os números inteiros de 1 até 100 utilizando while. Durante a repetição, some todos os números pares encontrados. Ao final, exiba:

A soma dos números pares entre 1 e 100 é: resultado

O programa não precisa solicitar dados ao usuário.

Restrição: Percorra todos os números de 1 até 100, avançando de um em um. Utilize uma condição para verificar se o número atual é par.
'''

even_sum = 0
current_number = 1
final_number = 100

while current_number <= final_number:
    if current_number % 2 == 0:
        even_sum += current_number
    current_number += 1

print(f"A soma dos números pares entre 1 e {final_number} é: {even_sum}")