fav_numbers = {
    'Alex': ['3', '33333'],
    'Konstantine': ['9'],
    'Alik': ['21'],
    'Dennis': [],
    'Max': ['100', '50']
}
for name, numbers in fav_numbers.items():
    if len(numbers) == 1:
        ending = 'favorite number is:'
        print(f"{name}'s {ending} {numbers}")
    elif len(numbers) == 0:
        ending = 'have no favorite numbers.'
        print(f"{name} {ending}")
    else:
        ending = 'favorite numbers are:'
        print(f"{name}'s {ending} {numbers}")
