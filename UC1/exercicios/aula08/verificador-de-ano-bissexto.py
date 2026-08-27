'''
1. Verificador de Ano Bissexto
Crie uma função chamada eh_bissexto(ano):
● A função deve receber um ano (inteiro) como parâmetro.
● Ela deve retornar True (Booleano) se o ano for bissexto, e False caso contrário.
● Regras do ano bissexto: É divisível por 4, exceto para anos divisíveis por 100, a
menos que sejam também divisíveis por 400. (Ex: 2000 e 2400 são bissextos; 1900
e 2100 não são).
● No programa principal, peça um ano ao usuário e imprima "O ano X É bissexto" ou
"O ano X NÃO é bissexto", baseado no retorno da função.
'''

SEPARATOR_WIDTH = 60

def is_leap_year(year):
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def separator(character):
    print(character * SEPARATOR_WIDTH)


separator("=")
print("Verificador de ano bissexto".center(SEPARATOR_WIDTH))
separator("=")

try:
    year = int(input("Digite um ano: "))
    separator("-")
    
    if is_leap_year(year):
        print(f"O ano {year} é bissexto.")
        separator("=")
    else:
        print(f"O ano {year} NÃO é bissexto.")
        separator("=")

except ValueError:
    print("Entrada inválida: Insira apenas valores numéricos.")
    separator("=")