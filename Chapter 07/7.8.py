sandwich_orders = ['egg sandwich', 'chicken sandwich', 'ham sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you a {sandwich.title()}.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
