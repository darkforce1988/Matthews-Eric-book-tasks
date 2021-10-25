age = 33
if age < 2:
    print('Baby')
elif age < 4:
    print('Kid')
elif age < 13:
    print('Child')
elif age < 20:
    print('Teen')
elif age < 65:
    print('Adult')
else:
    print('Old man')

fav_fruits = ['Apples', 'Oranges', 'Pears']
fruit = 'Strawberry'
if fruit in fav_fruits:
    print(f"You really like {fruit}")
fruit = 'Apples'
if fruit in fav_fruits:
    print(f"You really like {fruit}")
fruit = 'Oranges'
if fruit in fav_fruits:
    print(f"You really like {fruit}")
fruit = 'Lemons'
if fruit in fav_fruits:
    print(f"You really like {fruit}")
fruit = 'Pears'
if fruit in fav_fruits:
    print(f"You really like {fruit}")
