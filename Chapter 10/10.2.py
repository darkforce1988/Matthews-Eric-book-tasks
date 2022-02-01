file_name = 'learning_python.txt'

with open(file_name, encoding='UTF-8') as file_object:
    file_contents = file_object.read()
    print(f"The contents of a modified file '{file_name}':\n"
          f"{file_contents.replace('Python', 'JavaScript')}")

with open(file_name, encoding='UTF-8') as file_object:
    print(f"The contents of a modified file '{file_name}':")
    for line in file_object:
        print(line.rstrip().replace('Python', 'JavaScript'))
print()

with open(file_name, encoding='UTF-8') as file_object:
    file_contents = file_object.readlines()
    print(f"The contents of a modified file '{file_name}':")
for line in file_contents:
    line = line.replace('Python', 'JavaScript')
    print(line.rstrip())
