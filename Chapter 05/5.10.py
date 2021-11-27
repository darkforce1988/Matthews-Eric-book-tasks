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
    current_users_lower.append(user_lower.lower())
new_users = ['mAx', 'Lexa', 'Andrey', 'ALIK', 'Paciupa']
for user in new_users:
    if user.lower() in current_users_lower:
        print(f"User '{user}' already exists, choose another user name")
    else:
        print(f"You can use '{user}' user name")
