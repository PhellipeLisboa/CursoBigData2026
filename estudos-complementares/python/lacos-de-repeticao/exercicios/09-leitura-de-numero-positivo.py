'''
Exercício 9: leitura de número positivo

Nível: Básico

Conceitos praticados
- while True;
- validação repetida;
- try/except;
- break;
- distinção entre erro de conversão e valor inadequado.

Enunciado: Escreva um programa que solicite um número positivo ao usuário. O programa deverá continuar solicitando uma nova entrada enquanto o usuário:

- fornecer um valor não numérico;
- fornecer zero;
- fornecer um número negativo.

Quando um número válido for informado, o laço deverá terminar e o programa deverá exibir:

Número válido informado: valor

Mensagens esperadas

Para uma entrada não numérica: Entrada inválida: digite apenas valores numéricos.

Para um número menor ou igual a zero: Entrada inválida: o número deve ser maior que zero.

Restrições:
- utilize while True;
- utilize try/except;
- utilize break para encerrar o laço;
- não transforme números negativos em positivos com abs();
- não encerre o programa após a primeira entrada inválida;
- não utilize funções nesta primeira versão.
'''

while True:
    try:
        number = float(input("Digite um número positivo: "))

        if number <= 0:
            print("Entrada inválida: o número deve ser maior que zero.")
            continue

        break
    except ValueError:
        print("Entrada inválida: digite apenas valores numéricos.")

print(f"Número válido informado: {number}")