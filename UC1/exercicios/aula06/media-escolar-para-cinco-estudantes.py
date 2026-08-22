'''
Média Escolar para 5 Estudantes
Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
(if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().
'''

STUDENT_COUNT = 5
MIN_SCORE = 0
MAX_SCORE = 10
SEPARATOR_WIDTH = 65

def is_score_invalid(score):
    return score < MIN_SCORE or score > MAX_SCORE


results = []
approved_count = 0
reassessment_count = 0
failed_count = 0
averages_sum = 0

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
                    failed_count += 1
                elif average < 6:
                    status = "Recuperação :("
                    reassessment_count += 1
                else:
                    status = "Aprovado :)"
                    approved_count += 1

                results.append(f"Aluno: {name} | Média: {average:.2f} | Situação: {status}")
                averages_sum += average
                break
            else:
                print("Entrada inválida: insira valores válidos para as notas (0 a 10, ou -1 para a optativa).")
        except ValueError:
            print("=" * SEPARATOR_WIDTH)
            print("Entrada inválida: insira apenas valores numéricos.")
        
class_average = averages_sum / STUDENT_COUNT

print("=" * SEPARATOR_WIDTH)
print("RELATÓRIO".center(SEPARATOR_WIDTH))
print("=" * SEPARATOR_WIDTH)

for result in results:
    print(result)
    print("-" * SEPARATOR_WIDTH)

print(f"Média geral: {class_average:.2f} | Aprovados: {approved_count} | Recuperação: {reassessment_count} | Reprovados: {failed_count}")
print("=" * SEPARATOR_WIDTH)

    