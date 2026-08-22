'''
2. Cadastro de Candidatos
Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
candidatos menores de 18 anos.
● O programa deve pedir o Ano de Nascimento do candidato.
● Se for menor de 18, o programa deve informar que ele não pode participar e pular
a coleta dos demais dados (telefone, email etc) para esse candidato.
● Se for maior de 18, o programa prossegue com o input() para os demais dados.
'''

from datetime import date

CURRENT_YEAR = date.today().year
MAX_CANDIDATE_AGE = 100
MIN_YEAR_OF_BIRTH = CURRENT_YEAR - MAX_CANDIDATE_AGE
CANDIDATE_COUNT = 12
MIN_CANDIDATE_AGE = 18
SEPARATOR_WIDTH = 86

report = "=" * SEPARATOR_WIDTH + "\n"
report += "CANDIDATOS HABILITADOS".center(SEPARATOR_WIDTH) + "\n"
report += "=" * SEPARATOR_WIDTH + "\n"

for candidate_index in range(CANDIDATE_COUNT):
    while True:
        print("=" * SEPARATOR_WIDTH)
        print(f"Cadastro do {candidate_index + 1}º candidato".center(SEPARATOR_WIDTH))
        print("=" * SEPARATOR_WIDTH)

        name = input("Digite seu nome: ")

        try:
            year_of_birth = int(input("Digite seu ano de nascimento: "))
            
            if year_of_birth < MIN_YEAR_OF_BIRTH or year_of_birth > CURRENT_YEAR:
                print(f"Entrada inválida: informe um ano entre {MIN_YEAR_OF_BIRTH} e {CURRENT_YEAR}")
                continue
        
            age = CURRENT_YEAR - year_of_birth
            if age < MIN_CANDIDATE_AGE:
                print(f"Infelizmente apenas pessoas com {MIN_CANDIDATE_AGE} anos ou mais podem participar.")
                break
        
            phone_number = input("Digite seu telefone: ")
            email = input("Digite seu email: ")
            report += f"Nome: {name} | Idade: {age} | Telefone: {phone_number} | Email: {email}\n"
            report += "-" * SEPARATOR_WIDTH + "\n"
            
            break
        except ValueError:
            print("Entrada inválida: informe apenas valores numéricos inteiros para ano de nascimento.")

print(report)