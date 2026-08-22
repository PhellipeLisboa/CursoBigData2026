'''
1. Cálculo de Média Escolar para Vários Alunos
Use o laço for para repetir a lógica de cálculo de média e status
(Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.
'''

STUDENT_COUNT = 10
MIN_SCORE = 0
MAX_SCORE = 10
SEPARATOR_WIDTH = 58

def is_score_invalid(score):
    return score < MIN_SCORE or score > MAX_SCORE


report = "=" * SEPARATOR_WIDTH + "\n" + "RELATÓRIO".center(SEPARATOR_WIDTH) + "\n" + "=" * SEPARATOR_WIDTH + "\n"

for student_index in range(STUDENT_COUNT):
    while True:
        try: 
            print("=" * SEPARATOR_WIDTH)
            name = input(f"Insira o nome do {student_index + 1}º estudante: ")
            first_score = float(input("Insira a nota da primeira avaliação: "))
            second_score = float(input("Insira a nota da segunda avaliação: "))
            optional_score = float(input("Insira a nota da avaliação optativa (Digite -1 caso o aluno não tenha feito): "))

            scores_are_valid = True

            if is_score_invalid(first_score) or is_score_invalid(second_score):
                scores_are_valid = False
            
            if optional_score != -1 and is_score_invalid(optional_score):
                scores_are_valid = False

            if scores_are_valid:

                if optional_score != -1:
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
                report += "-" * SEPARATOR_WIDTH + "\n"
                break
            else:
                print("Entrada inválida: insira valores válidos para as notas (0 a 10, ou -1 para a optativa).")
        except ValueError:
            print("=" * SEPARATOR_WIDTH)
            print("Entrada inválida: insira apenas valores numéricos.")
        
print(report)