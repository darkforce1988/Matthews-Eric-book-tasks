file_name = 'learning_python.txt'

with open(file_name, encoding='UTF-8') as file_object:
    file_contents = file_object.read()
    print(f"The contents of a file '{file_name}':\n{file_contents}")

with open(file_name, encoding='UTF-8') as file_object:
    print(f"The contents of a file '{file_name}':")
    for line in file_object:
        print(line.rstrip())
print()

with open(file_name, encoding='UTF-8') as file_object:
    file_contents = file_object.readlines()
    print(f"The contents of a file '{file_name}':")
    for line in file_contents:
        print(line.rstrip())
