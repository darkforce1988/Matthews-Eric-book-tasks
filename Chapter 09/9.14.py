from random import choice

values_pool = (1, 8, 22, 'a', 't', 3, 5, 2, 11, 17, 21, 10, 'x', 'y', 'z')


def pick_combination(values_pool, combination_length=4):
    combination_list = []
    for i in range(combination_length):
        value = choice(values_pool)
        combination_list.append(value)
        values_pool.remove(value)
    return combination_list


my_ticket = pick_combination(list(values_pool))
print(f"Any ticket matching these four numbers or letters wins a prize:"
      f"\n{my_ticket}")
