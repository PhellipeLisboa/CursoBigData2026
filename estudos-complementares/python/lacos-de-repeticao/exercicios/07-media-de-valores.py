'''
Exercício 7: média de valores

Nível: Básico

Conceitos praticados
- entrada de dados dentro de um while;
- variável de controle;
- contador;
- acumulador;
- cálculo realizado após o laço;
- formatação de números decimais.

Enunciado: Escreva um programa que solicite ao usuário cinco números. O programa deverá:

1 - ler um número a cada repetição;
2 - acumular a soma dos valores informados;
3 - contar quantos valores foram lidos;
4 - calcular a média após o encerramento do laço;
5 - exibir o resultado com duas casas decimais.

Exemplo de interação:

Digite o 1º número: 8
Digite o 2º número: 5
Digite o 3º número: 7
Digite o 4º número: 4
Digite o 5º número: 6
Média dos valores: 6.00

Restrições: Utilize while para controlar a quantidade de entradas.

Não é necessário usar listas neste momento, pois ainda não estudamos esse tema.
'''


total = 0
count = 0

while count < 5:
    number = float(input(f"Digite o {count + 1}º número: "))
    total += number
    count += 1

average = total / count

print(f"Média dos valores: {average:.2f}")