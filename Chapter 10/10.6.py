try:
    first_number = int(input('Please enter the first number: '))
    second_number = int(input('Please enter the second number for addition: '))
except ValueError:
    print("You have entered an incorrect number.")
else:
    sum_numbers = first_number + second_number
    print(f"The sum is: {sum_numbers}.")
