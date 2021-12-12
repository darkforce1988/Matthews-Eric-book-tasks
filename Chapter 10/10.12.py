import json

filename = 'favorite_numbers.json'

try:
    with open(filename, encoding='UTF-8') as f:
        number = json.load(f)
        print(f"I know your favorite number! It's '{number}'!")
except FileNotFoundError:
    with open(filename, 'w', encoding='UTF-8') as f:
        number = input("Please enter your favorite number: ")
        json.dump(number, f)
