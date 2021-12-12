import json

favorite_number = input("Please enter your favorite number: ")

filename = 'favorite_numbers.json'

with open(filename, 'w', encoding='UTF-8') as f:
    json.dump(favorite_number, f)

with open(filename, encoding='UTF-8') as f:
    number = json.load(f)
    print(f"I know your favorite number! It's '{number}'!")
