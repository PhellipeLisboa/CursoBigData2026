'''
3. Tentativa de Login e Senha
Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
para digitar a senha correta.
● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
● Dê ao usuário 3 tentativas para acertar a combinação.
● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
break para sair do loop.
● Se a senha estiver errada, informe o erro e diminua o número de tentativas
restantes.
● Se as tentativas acabarem, imprima uma mensagem de bloqueio.
'''

MAX_ATTEMPTS = 3
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "123456"
SEPARATOR_WIDTH = 65


def are_credentials_valid(username_input, password_input):
    return username_input == CORRECT_USERNAME and password_input == CORRECT_PASSWORD


for attempt_index in range(MAX_ATTEMPTS):
    print("=" * SEPARATOR_WIDTH)

    remaining_attempts = MAX_ATTEMPTS - (attempt_index + 1)

    username_input = input("Usuário: ")
    password_input = input("Senha: ")

    if are_credentials_valid(username_input, password_input):
        print("-" * SEPARATOR_WIDTH)
        print("Logado com sucesso!")
        print("=" * SEPARATOR_WIDTH)
        break
    elif attempt_index < (MAX_ATTEMPTS - 1):
        print("-" * SEPARATOR_WIDTH)
        print(f"Credenciais inválidas. Tente novamente. (Tentativas restantes: {remaining_attempts})")
    else:
        print("-" * SEPARATOR_WIDTH)
        print("Login bloqueado: número máximo de tentativas atingido. Entre em contato com o suporte: 4002-8922.")
        print("=" * SEPARATOR_WIDTH)