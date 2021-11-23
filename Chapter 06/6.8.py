Kosha = {'pet_type': 'cat', 'pet_owner': 'Max Avramenko'}
Zver = {'pet_type': 'dog', 'pet_owner': 'Dmitry K.'}

pets = [Kosha, Zver]

for pet in pets:
    print(f"{pet['pet_owner']}'s pet is a {pet['pet_type']}.")
