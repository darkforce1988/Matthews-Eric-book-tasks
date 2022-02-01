file_name = 'reasons_you_like_programming.txt'

while True:
    reason = input("Please tell me why do you like programming? "
                   "Enter 'q' to quit: ")
    if reason == 'q':
        break
    with open(file_name, 'a', encoding='UTF-8') as file_object:
        file_object.write(reason + '\n')
    print("Thanks for your answer!\n")
