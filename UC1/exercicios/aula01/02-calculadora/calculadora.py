first_number = int(input("Insira o primeiro número: "))
second_number = int(input("Insira o segundo número: "))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

if first_number == 0 and second_number == 0:
    division = "indeterminado"
    mod = "indeterminado"
elif second_number == 0:
    division = "impossível"
    mod = "impossível"
else:
    division = first_number / second_number
    mod = first_number % second_number

print("===========================")
print(f"{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} * {second_number} = {multiplication}")
print(f"{first_number} / {second_number} = {division}")
print(f"{first_number} % {second_number} = {mod}")
print("===========================")