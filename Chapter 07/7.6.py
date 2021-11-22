active = True
while active:
    age = input("Enter your age." + "\n" + "Type 'quit' to exit: ")
    if str(age) == 'quit':
        break
    if int(age) < 3:
        ticket_price = "free"
    elif int(age) < 13:
        ticket_price = "10$"
    elif int(age) >= 13:
        ticket_price = "15$"
    print(f"A price of your ticket is: {ticket_price}.")
    active = False
