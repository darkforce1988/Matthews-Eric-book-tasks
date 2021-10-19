countries = ['Spain', 'France', 'UK', 'Norway', 'Iceland']
print(f"Мои любимые страны - {countries[:3]}")
print(f"Мои любимые страны - {countries[1:4]}")

middle = len(countries) // 2
print(f"Мои любимые страны - {countries[middle:middle + 3]}")

print(f"Мои любимые страны - {countries[-3:]}")
