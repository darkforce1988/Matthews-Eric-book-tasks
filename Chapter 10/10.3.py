filename = 'guest.txt'

guest_name = input('Здравствуйте, введите ваше имя: ')

with open(filename, 'w', encoding='UTF-8') as file_object:
    file_object.write(guest_name)
