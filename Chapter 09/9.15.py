from random import choice

values_pool = [1, 8, 22, 'a', 't', 3, 5, 2, 11, 17, 21, 10, 'x', 'y', 'z']
values_combination_lenght = 4

win_values = []
for i in range(values_combination_lenght):
    win_value = choice(values_pool)
    win_values.append(win_value)

my_ticket = []
tries = 0
while my_ticket != win_values:
    my_ticket.clear()
    for i in range(values_combination_lenght):
        my_ticket.append(choice(values_pool))
    tries += 1
print(f"Winning ticket is: {win_values}\n"
      f"Amount of tries to win the lottery: {tries}")
