file_name = 'reasons_you_like_programming.txt'
with open(file_name, 'a') as file_object:
    while True:
        reason = input('Напишите, почему Вам нравится программировать? '
                       'Для выхода введите "q": ')
        if reason == 'q':
            break
        file_object.write(reason + '\n')
