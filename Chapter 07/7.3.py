number = input('Enter a number. I will tell you if it can be divided by 10: ')
number = int(number)
if number % 10 == 0:
    print(f"Yes! Number {number} can be divided by 10!")
else:
    print(f"NOPE! Number {number} can't be divided by 10!")
