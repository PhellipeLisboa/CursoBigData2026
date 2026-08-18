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
    first_score = float(input("Insira a nota da primeira avaliação: "))
    second_score = float(input("Insira a nota da segunda avaliação: "))
    optional_score = float(input("Insira a nota da avaliação optativa (Digite -1 caso o aluno não tenha feito): "))
    print("==========================================================")

    if first_score < 0 or first_score > 10 or second_score < 0 or second_score > 10:
        raise ValueError("Insira valores válidos para as notas (0 a 10).")

    if optional_score != -1:
        if optional_score < 0 or optional_score > 10:
            raise ValueError("Insira um valor válido para a nota da avaliação optativa (0 a 10 ou -1).")
        
        if first_score <= second_score and optional_score > first_score:
            first_score = optional_score
        elif second_score < first_score and optional_score > second_score:
            second_score = optional_score

    average = (first_score + second_score) / 2 

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