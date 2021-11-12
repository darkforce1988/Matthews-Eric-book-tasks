guests = input('Welcome! Enter a number of guests for table reservation: ')
guests = int(guests)
if guests > 8:
    print("Please wait until we find you a table.")
else:
    print("Your table is ready.")
