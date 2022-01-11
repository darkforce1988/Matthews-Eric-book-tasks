from random import choice

values = [1, 8, 22, 'a', 't', 3, 5, 2, 11, 17, 21, 10, 'x', 'y', 'z']

win_values_list = []
for amount_of_win_values in range(4):
    win_value = choice(values)
    win_values_list.append(str(win_value))

print(f"Any ticket matching these four numbers or letters wins a prize:"
      f"\n\t{win_values_list}")
