'''
Cadastro Seletivo de Candidatos
Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
Adicione este Dicionário à lista: candidatos_validos.append(candidato).
'''

from datetime import date

CURRENT_YEAR = date.today().year
MAX_CANDIDATE_AGE = 100
MIN_YEAR_OF_BIRTH = CURRENT_YEAR - MAX_CANDIDATE_AGE
CANDIDATE_COUNT = 5
MIN_CANDIDATE_AGE = 18
SEPARATOR_WIDTH = 86

valid_candidates = []

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

            candidate = {
                'name': name,
                'age': age,
                'phone_number': phone_number,
                'email': email
            }

            valid_candidates.append(candidate)
            break
        except ValueError:
            print("Entrada inválida: informe apenas valores numéricos inteiros para ano de nascimento.")


print("=" * SEPARATOR_WIDTH) 
print("CANDIDATOS HABILITADOS".center(SEPARATOR_WIDTH))
print("=" * SEPARATOR_WIDTH) 

if valid_candidates:
    for candidate in valid_candidates:
        print(f"Nome: {candidate['name']} | Idade: {candidate['age']} | Telefone: {candidate['phone_number']} | Email: {candidate['email']}")
        print("-" * SEPARATOR_WIDTH)
else:
    print("Nenhum candidato habilitado foi registrado.")
    print("=" * SEPARATOR_WIDTH) 