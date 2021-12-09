filename = 'guest_book.txt'
with open(filename, 'w') as file_object:
    while True:
        guest_name = input('Здравствуйте, введите ваше имя. '
                           'Для выхода введите "q": ')
        if guest_name == 'q':
            break
        message = guest_name + ", добро пожаловать!"
        print(message)
        file_object.write(message + '\n')
