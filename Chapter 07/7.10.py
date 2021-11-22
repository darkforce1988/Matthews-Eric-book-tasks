vacation_responses = {}
asking = True
while asking:
    name = input("Please enter your name: ")
    response = input("Describe a vacation you dream of: ")
    vacation_responses[name] = response
    response_end = input("Do you want to continue a survey? (yes/no) ")
    if response_end == 'no':
        asking = False
for name, response in vacation_responses.items():
    print(f"\nHere's the vacation that {name} is dreaming of: {response}.")
