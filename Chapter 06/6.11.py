cities = {
    'London': {
        'country': 'England',
        'population': '9,425,622',
        'fact': 'It is a very common mistake, but Big Ben is actually not the '
            'name for the iconic Tower in London. Big Ben is actually the name'
            'for the clock in the Tower.'
        },

    'Paris': {
        'country': 'France',
        'population': '11,078,546',
        'fact': 'around 5 million people per day use Paris Metro. After Moscow,'
            ' it’s the busiest underground network in Europe.'
        },

    'NY': {
        'country': 'United States',
        'population': '8,820,125',
        'fact': 'Honking your horn in NY is illegal.'
        }
}

for city, infos in cities.items():
    print(f"{city} info:")
    for info, value in infos.items():
        print(f"\t{info}: {value}")
