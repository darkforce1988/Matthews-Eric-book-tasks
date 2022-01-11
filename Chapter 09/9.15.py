from random import choice

values = [1, 8, 22, 'a', 't', 3, 5, 2, 11, 17, 21, 10, 'x', 'y', 'z']

win_values_list = []
for amount_of_win_values in range(4):
    win_value = choice(values)
    win_values_list.append(str(win_value))

my_ticket = []
tries = 0
while my_ticket != win_values_list:
    my_ticket.clear()
    for values_for_try in range(4):
        values_for_try = choice(values)
        my_ticket.append(str(values_for_try))
    tries += 1
print(f"Amount of tries for ticket match: {tries}")
