top_lakes = {'Superior': 'Canada', 'Victoria': 'Uganda', 'Baikal': 'Russia'}

for lake, country in top_lakes.items():
    print(f"The {lake.title()} runs through {country.title()}.")
print()

for lake in top_lakes:
    print(lake)
print()

for country in top_lakes.values():
    print(country)
