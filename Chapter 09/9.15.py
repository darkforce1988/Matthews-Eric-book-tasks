from random import choice

COMBINATION_LENGHT = 4
values_pool = (1, 8, 22, 'a', 't', 3, 5, 2, 11, 17, 21, 10, 'x', 'y', 'z')


def pick_combination(values=values_pool,
                     values_combination_lenght=COMBINATION_LENGHT):
    combination_list = []
    while len(combination_list) < values_combination_lenght:
        value = choice(values)
        if value not in combination_list:
            combination_list.append(value)
    return combination_list


win_ticket = pick_combination()

my_ticket = pick_combination()
tries = 0
while my_ticket != win_ticket:
    my_ticket = pick_combination()
    tries += 1

print(f"Winning ticket is: {win_ticket}\n"
      f"Amount of tries to win the lottery: {tries}")
