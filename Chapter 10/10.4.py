filename = 'guest_book.txt'

while True:
    guest_name = input("Hello! Please enter your name. "
                       "Enter 'q' to quit: ")
    if guest_name == 'q':
        break
    message = guest_name + ", welcome!"
    print(message)
    with open(filename, 'a', encoding='UTF-8') as file_object:
        file_object.write(message + "\n")
    print(f"Added a greeting message for {guest_name} to a guest book.\n")
