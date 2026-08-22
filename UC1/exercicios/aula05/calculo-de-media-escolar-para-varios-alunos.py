'''
1. Cálculo de Média Escolar para Vários Alunos
Use o laço for para repetir a lógica de cálculo de média e status
(Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.
'''

STUDENT_COUNT = 10
MIN_SCORE = 0
MAX_SCORE = 10
REPORT_WIDTH = 58

def is_invalid(score):
    return score < MIN_SCORE or score > MAX_SCORE


report = "=" * REPORT_WIDTH + "\n" + "RELATÓRIO".center(REPORT_WIDTH) + "\n" + "=" * REPORT_WIDTH + "\n"

registered_students = 0

while registered_students < STUDENT_COUNT:
    print("=" * REPORT_WIDTH)
    try: 
        name = input(f"Insira o nome do {registered_students + 1}º estudante: ")
        first_score = float(input("Insira a nota da primeira avaliação: "))
        second_score = float(input("Insira a nota da segunda avaliação: "))
        optional_score = float(input("Insira a nota da avaliação optativa (Digite -1 caso o aluno não tenha feito): "))

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

        report += f"Aluno: {name} | Média: {average:.2f} | Situação: {status}\n"
        report += "-" * REPORT_WIDTH + "\n"
        registered_students += 1

    except ValueError as error:
        print(f"Entrada inválida: {error}")
        
print(report)