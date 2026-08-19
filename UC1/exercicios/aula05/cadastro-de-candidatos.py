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
candidate_count = 12
candidates_report = "======================================================================================\n"
candidates_report += "                                CANDIDATOS HABILITADOS                                \n"
candidates_report += "======================================================================================\n"

for candidate_index in range(candidate_count):
    print("======================================================================================")
    print(f"                              Cadastro do {candidate_index + 1}º candidato                     ")
    print("======================================================================================")

    name = input("Digite seu nome: ")
    year_of_birth = int(input("Digite seu ano de nascimento: "))

    if CURRENT_YEAR < year_of_birth:
        print(f"Entrada inválida: o ano de nascimento não pode ser maior que {CURRENT_YEAR}")
        continue

    age = CURRENT_YEAR - year_of_birth
    if age < 18:
        print(f"Infelizmente apenas pessoas com 18 anos ou mais podem participar.")
        continue

    phone_number = input("Digite seu telefone: ")
    email = input("Digite seu email: ")
    candidates_report += f"Nome: {name} | Idade: {age} | Telefone: {phone_number} | Email: {email}\n--------------------------------------------------------------------------------------\n"

print(candidates_report)