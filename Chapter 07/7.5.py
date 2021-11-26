active = True

while active:
    age = int(input("Enter your age: "))
    if age < 3:
        ticket_price = "free"
    elif 13 > age >= 3:
        ticket_price = "$10"
    elif age >= 13:
        ticket_price = "$15"
    print(f"A price of your ticket is: {ticket_price}.")
