# Sintaxe básica do try/except

try:
    # Código que possivelmente irá gerar um exceção
    result = 10 / 0

except ZeroDivisionError:
    # Código executado se esse tipo de erro ocorrer
    print("Não é possível dividir por zero.")


# Guardando o objeto da exceção

try:
    number = int("abc")

except ValueError as erro:
    print(f"Ocorreu um erro: {erro}")


# É possível tratar multiplas exceções

try:
    number = int(input("Digite um número: "))
    result = 10 / number
except ValueError:
    print("Você precisa informar um número válido.")
except ZeroDivisionError:
    print("O número não pode ser zero.")

# OBS: Também é possível agrupar exceções quando o tratamento para elas for igual:

try:
    number = int(input("Digite um número: "))
    result = 10 / number
except (ValueError, ZeroDivisionError) as erro:
    print(f"Operação inválida: {erro}")


# Estrutura completa

try:
    # Código que pode falhar
    number = int("10")
except ValueError:
    # Bloco executado se ocorrer ValueError
    print("Valor inválido")
else:
    # Bloco executado somente se nenhuma exceção ocorrer
    print(f"Número convertido: {number}")
finally:
    # Bloco executado sempre, havendo erro ou não
    print("Processamento encerrado.")


# OBS: Uma boa prática é evitar capturar exceções de maneira genérica, sempre buscar capturar exceções específicas para que erros inesperados não fiquem escondidos e a depuração se torne mais fácil.