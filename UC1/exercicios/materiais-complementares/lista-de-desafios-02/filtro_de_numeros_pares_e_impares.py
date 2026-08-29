    
def separar_pares_e_impares(numbers):
    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return {
        "even_numbers" : even,
        "odd_numbers": odd
    }


numbers = [2, 3, 5, 7, 33, 42, 57, 90]
print(separar_pares_e_impares(numbers))