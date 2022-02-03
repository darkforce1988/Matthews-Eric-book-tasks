from random import choice

print("Welcome to M&J lottery! There are lottery rules:\n"
      "- you'll get a ticket with 5 random values from the pool of 15 values;\n"
      "- we'll compare the values of your ticket with win values\n"
      "- just consecutive mathes will be counted!\n"
      "- keep in mind that your odds of winning are TINY!!!\n")

values_pool = (1, 8, 22, 'a', 't', 3, 5, 2, 11, 17, 21, 10, 'x', 'y', 'z')


def pick_combination(values=values_pool, combination_length=4):
    combination_list = []
    while len(combination_list) < combination_length:
        value = choice(values)
        if value not in combination_list:
            combination_list.append(value)
    return combination_list


win_combination = pick_combination()

my_ticket = pick_combination()
tries = 1
while my_ticket != win_combination:
    my_ticket = pick_combination()
    tries += 1

print(f"Winning ticket is: {my_ticket}\n"
      f"Amount of tries to win the lottery: {tries}")
