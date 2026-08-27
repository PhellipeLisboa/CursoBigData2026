# Aula 08 - Dia 26/08/2026
# Tema principal: Funções

def calculadora_v1(num1, num2, operador="3"):
    
    match operador:
        case "1":
            resultado = num1 + num2
        case "2": 
            resultado = num1 - num2
        case "3": 
            resultado = num1 * num2
        case "4": 
            if num2 != 0:
                divisao = num1 / num2
                resultado = divisao
            else:
                print("Entrada inválida: Não é possível dividir por zero.")
        case _: 
            print("Entrada inválida: Insira um operador válido.")

    return resultado

num1 = float(input("Digite seu primeiro número: "))
num2 = float(input("Digite seu segundo número: "))

print("Informe a operação desejada entre:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operador = input("Operação desejada: ")

calculinho = calculadora_v1(num1, num2, operador)
calculinho