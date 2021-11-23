sandwich_orders = ['pastrami', 'egg sandwich', 'pastrami',
                   'chicken sandwich', 'ham sandwich', 'pastrami',
                   ]
finished_sandwiches = []

print("Sorry, we can't make 'pastrami' sandwich for You!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you {sandwich.title()}.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
