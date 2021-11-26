Jan = {
    'first_name': 'Jan',
    'last_name': 'Patsiupa',
    'age': 45,
    'city': 'Drichin',
}

Max = {
    'first_name': 'Maxim',
    'last_name': 'Auramenka',
    'age': 33,
    'city': 'Minsk',
}

Alex = {
    'first_name': 'Alexander',
    'last_name': 'Vedro',
    'age': 27,
    'city': 'Minsk',
}

people = [Jan, Max, Alex]
for name in people:
    full_name = f"{name['first_name']} {name['last_name']}"
    print(f"Info about {full_name}:\n\tAge: {name['age']}\n\tCity: {name['city']}")
