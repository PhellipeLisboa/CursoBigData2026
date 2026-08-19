'''
Exercício 10: média de cargas válidas

Nível: Intermediário

Conceitos praticados:
- repetição com quantidade definida;
- repetição de entradas inválidas;
- try/except;
- contador;
- acumulador;
- validação de regra;
- cálculo de média;
- combinação de laços.

Enunciado: Uma pessoa deseja registrar as cargas utilizadas em cinco séries válidas de um exercício de musculação. O programa deverá solicitar a carga, em quilogramas, utilizada em cada série. Uma carga será considerada válida quando:

- puder ser convertida para um número;
- for maior que zero.

Quando a entrada for inválida, o programa deverá:

- apresentar uma mensagem adequada;
- solicitar novamente a carga da mesma série;
- não acrescentar o valor ao total;
- não avançar para a próxima série.

Depois de registrar cinco cargas válidas, o programa deverá exibir:

Carga total movimentada: valor kg
Carga média por série: valor kg

OBS: Apresente a média com duas casas decimais.

Requisitos
Registre exatamente cinco cargas válidas.
Utilize while.
Utilize try/except.
Não utilize listas.
Não utilize funções nesta versão.
Não utilize abs() para converter cargas negativas.
Calcule o total utilizando um acumulador.
Calcule a média somente depois que todas as cargas válidas forem registradas.

Mensagens para entradas inválidas

Quando a conversão falhar: Entrada inválida: digite apenas valores numéricos.

Quando a carga for menor ou igual a zero: Entrada inválida: a carga deve ser maior que zero.
'''

SERIES_COUNT = 5

total_load = 0
load_count = 0

while load_count < SERIES_COUNT:

    try:
        load = float(input(f"Digite a carga da {load_count + 1}ª série em kg: "))

        if load <= 0:
            print("Entrada inválida: a carga deve ser maior que zero.")
            continue

        total_load += load
        load_count += 1
    except ValueError:
        print("Entrada inválida: digite apenas valores numéricos.")

average_load = total_load / load_count

print(f"Carga total movimentada: {total_load:.2f} kg")
print(f"Carga média por série: {average_load:.2f} kg")