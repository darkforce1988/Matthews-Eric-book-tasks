fav_numbers = {
    'Alex': [3, 33333],
    'Konstantine': [9],
    'Alik': [21],
    'Dennis': [],
    'Max': [100, 50]
}

for name, numbers in fav_numbers.items():
    if len(numbers) == 1:
        for number in numbers:
            print(f"{name}'s favorite number is: {number}.")
    elif len(numbers) == 0:
        print(f"{name} have no favorite numbers.")
    else:
        print(f"{name}'s favorite numbers are: {', '.join(map(str, numbers))}.")

#       print(*numbers, sep=', ')
