from random import choice

values_pool = [1, 8, 22, 'a', 't', 3, 5, 2, 11, 17, 21, 10, 'x', 'y', 'z']

win_values = []
for i in range(4):
    win_value = choice(values_pool)
    win_values.append(win_value)
    values_pool.remove(win_value)

print(f"Any ticket matching these four numbers or letters wins a prize:"
      f"\n\t{win_values}")
