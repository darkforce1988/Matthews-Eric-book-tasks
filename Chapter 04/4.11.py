max_pizzas = ['pizza', 'falafel', 'carrot cake']
jan_pizzas = max_pizzas[:]
max_pizzas.append('mozarella')
jan_pizzas.append('dranik')
print(max_pizzas)
print(jan_pizzas)

for pizza in max_pizzas:
    print(pizza.title(), end=' или ')

print(max_pizzas[0], max_pizzas[2], sep=' ИЛИ ')
