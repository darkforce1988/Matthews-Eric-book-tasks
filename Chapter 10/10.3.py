filename = 'guest.txt'

guest_name = input("Hello! Please enter your name: ")

with open(filename, 'w', encoding='UTF-8') as file_object:
    file_object.write(guest_name)
    print(f"{guest_name}, we'll add you to our guest book!")
