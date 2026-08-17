name = input("Insira o nome do aluno: ")
first_grade = float(input("Insira a primeira nota: "))
second_grade = float(input("Insira a segunda nota: "))

average = (first_grade + second_grade) / 2

print(f"A nota de {name} na primeira avaliação foi {first_grade} e na segunda avaliação foi {second_grade}, portanto sua média é {average:.1f}")