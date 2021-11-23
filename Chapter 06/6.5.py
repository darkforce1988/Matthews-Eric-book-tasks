top_lakes = {'Superior': 'Canada', 'Victoria': 'Uganda', 'Baikal': 'Russia'}

for key, value in top_lakes.items():
    print(f"The {key.title()} runs through {value.title()}.")
print()

for key in top_lakes:
    print(key)
print()

for value in top_lakes.values():
    print(value)
