# Desafio2: Cálculo de média e status do estudante
'''
Dadas as 4 notas de um estudante, calcule sua média e, com base nela, emita a mensagem
de status correspondente:
1. Aprovado: Média estritamente maior que 7.
2. Recuperação: Média entre 5 (inclusive) e 7 (inclusive).
3. Reprovação: Média estritamente abaixo de 5.
'''
print("==========================================================")
name = input("Insira o nome do estudante: ")
first_grade = float(input("Insira a primeira nota: "))
second_grade = float(input("Insira a segunda nota: "))
third_grade = float(input("Insira a terceira nota: "))
fourth_grade = float(input("Insira a quarta nota: "))

average = (first_grade + second_grade + third_grade + fourth_grade) / 4
print("----------------------------------------------------------")
if average < 5:
    print(f"Aluno: {name} | Média: {average:.2f} | Situação: Reprovado :(")
elif average <= 7:
    print(f"Aluno: {name} | Média: {average:.2f} | Situação: Recuperação :(")
else:
    print(f"Aluno: {name} | Média: {average:.2f} | Situação: Aprovado :)")
print("==========================================================")