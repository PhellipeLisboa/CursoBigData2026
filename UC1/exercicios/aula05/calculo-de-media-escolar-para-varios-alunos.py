'''
1. Cálculo de Média Escolar para Vários Alunos
Use o laço for para repetir a lógica de cálculo de média e status
(Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.
'''

def is_invalid(score):
    return score < 0 or score > 10


STUDENT_COUNT = 10
result = "==========================================================\n"

for student_index in range(STUDENT_COUNT):
    print("==========================================================")
    name = input(f"Insira o nome do {student_index + 1}º estudante: ")
    first_score = float(input("Insira a primeira nota: "))
    second_score = float(input("Insira a segunda nota: "))
    third_score = float(input("Insira a terceira nota: "))
    fourth_score = float(input("Insira a quarta nota: "))

    if is_invalid(first_score) or is_invalid(second_score) or is_invalid(third_score) or is_invalid(fourth_score):
        print("Entrada inválida: notas devem estar no intervalo de 0 a 10.")
        break

    average = (first_score + second_score + third_score + fourth_score) / 4
    
    if average < 5:
        status = "Reprovado :("
    elif average <= 7:
        status = "Recuperação :("
    else:
        status = "Aprovado :)"

    result += f"Aluno: {name} | Média: {average:.2f} | Situação: {status}\n"
    result += "----------------------------------------------------------\n"

print(result)