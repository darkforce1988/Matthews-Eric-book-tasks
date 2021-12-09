import json

filename = 'favorite_numbers.json'

try:
    with open(filename) as f:
        number = json.load(f)
        print(f"I know your favorite number! It's '{number}'!")
except FileNotFoundError:
    with open(filename, 'w') as f:
        number = input("Please enter your favorite number: ")
        json.dump(number, f)
