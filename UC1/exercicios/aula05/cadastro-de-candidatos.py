'''
2. Cadastro de Candidatos
Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
candidatos menores de 18 anos.
● O programa deve pedir o Ano de Nascimento do candidato.
● Se for menor de 18, o programa deve informar que ele não pode participar e pular
a coleta dos demais dados (telefone, email etc) para esse candidato.
● Se for maior de 18, o programa prossegue com o input() para os demais dados.
'''

CURRENT_YEAR = 2026
CANDIDATE_COUNT = 12
MIN_CANDIDATE_AGE = 18
MIN_YEAR_OF_BIRTH = 1900

candidates_report = "======================================================================================\n"
candidates_report += "                                CANDIDATOS HABILITADOS                                \n"
candidates_report += "======================================================================================\n"

for candidate_index in range(CANDIDATE_COUNT):
    print("======================================================================================")
    print(f"                              Cadastro do {candidate_index + 1}º candidato                     ")
    print("======================================================================================")

    name = input("Digite seu nome: ")
    year_of_birth = int(input("Digite seu ano de nascimento: "))

    if year_of_birth < MIN_YEAR_OF_BIRTH or CURRENT_YEAR < year_of_birth:
        print(f"Entrada inválida: Informe um ano entre {MIN_YEAR_OF_BIRTH} e {CURRENT_YEAR}")
        continue

    age = CURRENT_YEAR - year_of_birth
    if age < MIN_CANDIDATE_AGE:
        print(f"Infelizmente apenas pessoas com {MIN_CANDIDATE_AGE} anos ou mais podem participar.")
        continue

    phone_number = input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    candidates_report += f"Nome: {name} | Idade: {age} | Telefone: {phone_number} | Email: {email}\n--------------------------------------------------------------------------------------\n"

print(candidates_report)