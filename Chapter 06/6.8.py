Kosha = {'pet_name': 'Kosha', 'pet_type': 'cat', 'pet_owner': 'Max Avramenko'}
Zver = {'pet_name': 'Zver', 'pet_type': 'dog', 'pet_owner': 'Dmitry K.'}

pets = [Kosha, Zver]

for pet in pets:
    print(f"{pet['pet_name']} is a {pet['pet_type']}. {pet['pet_owner']} is it's owner.")
