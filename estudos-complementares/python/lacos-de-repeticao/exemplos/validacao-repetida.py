while True:
    try:
        number = float(input("Digite um número positivo: "))

        if number <= 0:
            print("Entrada inválida: o número deve ser maior que zero.")
            continue

        break

    except ValueError:
        print("Entrada inválida: digite apenas valores numéricos.")

print(f"Número válido informado: {number}")