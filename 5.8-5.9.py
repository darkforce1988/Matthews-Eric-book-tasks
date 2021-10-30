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
