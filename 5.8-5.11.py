accounts = ['force', 'jan', 'admin', 'asshole', 'pasiypa']
if accounts:
    for account in accounts:
        if account == 'admin':
            print("Hello, Admin, glad to see you again!")
        else:
            print(f"Hello, {account.title()}!")
else:
    print("We need to invite some users!")

accounts = []
if accounts:
    for account in accounts:
        if account == 'admin':
            print("Hello, Admin, glad to see you again!")
        else:
            print(f"Hello, {account.title()}!")
else:
    print("We need to invite some users!")

current_users = ['max', 'jan', 'kostya', 'alik', 'romik']
new_users = ['mAx', 'Lexa', 'Andrey', 'ALIK', 'Paciupa']
for user in new_users:
    if user.lower() in current_users:
        print(f"User '{user}' already exists, choose another user name")
    else:
        print(f"You can use '{user}' user name")

current_users = ['Max', 'JAN', 'kosTYA', 'aliK', 'Romik']
current_users_lower = []
for user_lower in current_users:
    user_lower = user_lower.lower()
    current_users_lower.append(user_lower)
new_users = ['mAx', 'Lexa', 'Andrey', 'ALIK', 'Paciupa']
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"User '{user}' already exists, choose another user name")
    else:
        print(f"You can use '{user}' user name")

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in numbers:
    if number == '1':
        print(f'{number}st')
    elif number == '2':
        print(f'{number}nd')
    elif number == '3':
        print(f'{number}rd')
    else:
        print(f'{number}th')
