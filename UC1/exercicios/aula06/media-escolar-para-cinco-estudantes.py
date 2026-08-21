'''
Média Escolar para 5 Estudantes
Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
(if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().
'''

STUDENT_COUNT = 5
MIN_SCORE = 0
MAX_SCORE = 10
REPORT_WIDTH = 65

def is_invalid(score):
    return score < MIN_SCORE or score > MAX_SCORE


results = []
approved_count = 0
reassessment_count = 0
failed_count = 0
averages_sum = 0

for student_index in range(STUDENT_COUNT):
    print("=" * REPORT_WIDTH)

    try:
        name = input(f"Insira o nome do {student_index + 1}º estudante: ")
        first_score = float(input("Insira a primeira nota: "))
        second_score = float(input("Insira a segunda nota: "))
        third_score = float(input("Insira a terceira nota: "))
        fourth_score = float(input("Insira a quarta nota: "))

        if is_invalid(first_score) or is_invalid(second_score) or is_invalid(third_score) or is_invalid(fourth_score):
            print("Entrada inválida: notas devem estar no intervalo de 0 a 10.")
            continue

        average = (first_score + second_score + third_score + fourth_score) / 4
        
        if average < 5:
            status = "Reprovado :("
            failed_count += 1
        elif average <= 7:
            status = "Recuperação :("
            reassessment_count += 1
        else:
            status = "Aprovado :)"
            approved_count += 1

        results.append(f"Aluno: {name} | Média: {average:.2f} | Situação: {status}")
        averages_sum += average
    except ValueError:
        print("Entrada inválida: insira apenas valores numéricos.")
        continue

valid_students_count = len(results)

if valid_students_count == 0:
    print("=" * REPORT_WIDTH)
    print("Nenhum resultado válido foi registrado.")
else:
    class_average = averages_sum / valid_students_count

    print("=" * REPORT_WIDTH)
    print("RELATÓRIO".center(REPORT_WIDTH))
    print("=" * REPORT_WIDTH)

    for result in results:
        print(result)
        print("-" * REPORT_WIDTH)

    print(f"Média geral: {class_average:.2f} | Aprovados: {approved_count} | Recuperação: {reassessment_count} | Reprovados: {failed_count}")
    print("=" * REPORT_WIDTH)

    