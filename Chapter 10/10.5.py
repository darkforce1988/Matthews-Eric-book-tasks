file_name = 'reasons_you_like_programming.txt'

while True:
    reason = input('Напишите, почему Вам нравится программировать? '
                   'Для выхода введите "q": ')
    if reason == 'q':
        break
    with open(file_name, 'a', encoding='UTF-8') as file_object:
        file_object.write(reason + '\n')
