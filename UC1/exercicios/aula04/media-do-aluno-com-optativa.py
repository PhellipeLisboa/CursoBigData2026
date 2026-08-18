'''
5. Média do Aluno com Optativa:
Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
recuperação, de acordo com as informações abaixo:
Aprovado: média >= 6.0
Reprovado: média < 3.0
Recuperação: média >= 3.0 e < 6.0
Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
resultado final.
'''

try:
    print("==========================================================")
    first_grade = float(input("Insira a nota da primeira avaliação: "))
    second_grade = float(input("Insira a nota da segunda avaliação: "))
    optative_grade = float(input("Insira a nota da avaliação optativa (Digite -1 caso o aluno não tenha feito): "))
    print("==========================================================")

    if first_grade < 0 or first_grade > 10 or second_grade < 0 or second_grade > 10:
        raise ValueError("Insira valores válidos para as notas (0 - 10).")

    if optative_grade != -1:
        if first_grade < second_grade and optative_grade > first_grade:
            first_grade = optative_grade
        elif second_grade < first_grade and optative_grade > second_grade:
            second_grade = optative_grade

        average = (first_grade + second_grade) / 2 
    else:
        average = (first_grade + second_grade) / 2 

    if average < 3:
        status = "Reprovado :("
    elif average < 6:
        status = "Recuperação :("
    else: 
        status = "Aprovado :)"

    print(f"Média: {average:.2f} | Situação: {status}")
    print("==========================================================")
except ValueError as error:
    print(f"Entrada inválida: {error}")