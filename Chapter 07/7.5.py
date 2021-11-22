age = int(input("Enter your age: "))
if age < 3:
    ticket_price = 'free'
elif age < 13:
    ticket_price = "10$"
else:
    ticket_price = "15$"
print(f"A price of your ticket is: {ticket_price}.")
