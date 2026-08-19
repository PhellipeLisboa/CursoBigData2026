# Laços de repetição em Python

Laços de repetição são estruturas que possibilitam a execução de um trecho de código várias vezes.

## `while`

O `while` executa um bloco de código repetidamente enquanto sua condição for avaliada como verdadeira.

### Estrutura

```python
while condition:
    # Código a ser repetido
```

### Elementos principais

Um `while` controlado por uma variável normalmente contém três partes importantes:

- Inicialização : Defino o valor inicial da variável de controle.
- Condição      : Determina se o laço deve continuar.
- Atualização   : Modifica a variável de controle e permite que o laço se aproxime do encerramento.

### Exemplo

```Python
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1
```

## Laços infinitos

Um laço pode continuar indefinidamente quando sua condição nunca se torna falsa, por isso é importante observar como as variáveis utilizadas na condição são modificadas durante a execução do código.

## Contadores

Um contador é uma variável utilizada para registrar quantas vezes determinada situação ocorre.

De modo geral, um contador é iniciado em zero e é incrementado quando uma ocorrência é identificada.

### Exemplo

```python
count = 0
current_number = 1

while current_number <= 10: 
    if current_number % 2 == 0:
        count += 1
    current_number += 1
```

A variável *current_number* controla a repetição, enquanto *count* registra quantos números pares foram encontrados.

## Acumuladores

Um acumulador armazena um resultado construído gradualmente durante as repetições.

Em uma soma, o acumulador normalmente começa em zero, já que este é o elemento neutro da soma. Naturalmente, em uma multiplicação o acumulador normalmente começa em um.

### Exemplo

```python
total = 0
current_number = 1

while current_number <= 5:
    total += current_number
    current_number += 1
```

A cada repetição, o valor de *current_number* é acrescentado a total.

## Diferença entre contador e acumulador

- Um contador registra o número de ocorrências
- Um acumulador armazena a soma ou outro resultado formado pelos valores processados 

## Validação repetida de entradas

Laços de repetição podem ser utilizados para solicitar novamente uma entrada quando o usuário fornece um valor inválido.

Esse tipo de repetição é adequado quando não sabemos antecipadamente quantas tentativas serão necessárias.

### break

O comando break encerra imediatamente o laço mais próximo.

Em uma validação repetida, ele deve ser executado somente depois que a entrada atender a todas as regras.

### continue

O comando continue interrompe a repetição atual e inicia a próxima.

Ele pode ser utilizado quando uma entrada não deve continuar sendo processada.

### Validação com `while True`

A estrutura `while True` cria um laço cuja condição permanece verdadeira. Seu encerramento pode ser controlado com `break`.

### Validação de conversão

A validação de conversão verifica se a entrada pode ser tranformada no tipo esperado.

Por exemplo, float() lança ValueError quando recebe um texto que não apresenta um número.

```python
while True:
    try:
        number = float(input("Digite um número: "))
        break
    except ValueError:
        print("Entrada inválida: digite apenas valores numéricos.")
```

### Validação da regra do problema

Uma entrada pode ser numericamente válida, mas não atender às regras do programa.

```python
while True:
    try:
        number = float(input("Digite um número positivo: "))

        if number <= 0:
            print("Entrada inválida: o número deve ser maior que zero.")
            continue

        break

    except ValueError:
        print("Entrada inválida: digite apenas valores numéricos.")
```
