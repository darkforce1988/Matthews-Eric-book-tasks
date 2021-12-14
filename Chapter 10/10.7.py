while True:
    try:
        first_number = input('Enter the first number. Type "q" to quit: ')
        if first_number == 'q':
            break
        first_number = int(first_number)
        second_number = input('Enter the second number to make addition: ')
        if second_number == 'q':
            break
        second_number = int(second_number)
    except ValueError:
        print("You have entered an incorrect number.")
    else:
        sum_numbers = first_number + second_number
        print(f"The sum is: {sum_numbers}.")
