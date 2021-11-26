message = "When you are ready to make your order - type 'quit'."
message += "\nPlease enter a topping for your pizza: "
topping = ""
toppings = []

while True:
    topping = input(message)
    if topping == 'quit':
        break
    print(f"We will add a {topping} to your pizza!")
    toppings.append(topping)

print(f"We'll make your pizza ready in a short time.\nSelected "
      f"toppings: {toppings}.")
