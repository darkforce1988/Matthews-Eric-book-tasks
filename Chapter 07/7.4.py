message = "When you are ready to make your order - type 'quit'."
message += " Please enter a topping for your pizza: "
topping = ""
toppings = []
while topping != 'quit':
    topping = input(message)
    if topping == 'quit':
        break
    toppings.append(topping)

print(f"We'll make your pizza ready in a short time.\nSelected "
    f"'toppings: {toppings}.")
