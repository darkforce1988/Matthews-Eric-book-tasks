favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_voting = []
for people in favorite_languages:
    people_voting.append(people)

people_voting.append('max')
people_voting.append('paciupa')

for people in people_voting:
    if people in favorite_languages:
        print(f"{people.title()}, thank you for responding!")
    else:
        print(f"{people.title()}, we invite you to take the poll!")
