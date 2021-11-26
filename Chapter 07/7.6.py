active = True

while active:
    age = input("Enter your age." + "\n" + "Type 'quit' to exit: ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        ticket_price = "free"
    elif 13 > age >= 3:
        ticket_price = "$10"
    elif age >= 13:
        ticket_price = "$15"
    print(f"A price of your ticket is: {ticket_price}.")
    active = False
