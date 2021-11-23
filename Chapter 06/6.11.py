cities = {
    'London': {
        'country': 'England',
        'population': '9,425,622',
        'fact': 'It is a very common mistake, but Big Ben is actually not the '
            'name for the iconic Tower in London. Big Ben is actually the name'
            ' for the clock in the Tower.'
        },

    'Paris': {
        'country': 'France',
        'population': '11,078,546',
        'fact': 'Around 5 million people per day use Paris Metro. After Moscow,'
            ' it’s the busiest underground network in Europe.'
        },

    'NY': {
        'country': 'United States',
        'population': '8,820,125',
        'fact': 'Honking your horn in NY is illegal.'
        }
}

for city, infos in cities.items():
    country = infos['country']
    population = infos['population']
    fact = infos['fact']
    print(f"{city} info:")
    print(f"\tThis city is situated in {country}.")
    print(f"\tPopulation of this city is {population}.")
    print(f"\tInteresting fact about {city}: {fact}.")
