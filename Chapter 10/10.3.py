filename = 'guest.txt'
with open(filename, 'w') as file_object:
    guest_name = input('Здравствуйте, введите ваше имя: ')
    message = guest_name + ", добро пожаловать!"
    file_object.write(message)
