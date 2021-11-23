favorite_places = {
    'Jan': ['Drichin', 'Pharmacy number 112'],
    'Max': ['Lodnon', 'Brussels']
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are: ")

    for place in places:
        print(f"\t{place}")
