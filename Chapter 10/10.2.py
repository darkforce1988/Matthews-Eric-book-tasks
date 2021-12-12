with open('learning_python.txt', encoding='UTF-8') as txt_file_object:
    txt_file_contents = txt_file_object.read()
    print(txt_file_contents.replace('Python', 'JavaScript'))

with open('learning_python.txt', encoding='UTF-8') as txt_file_object:
    for line in txt_file_object:
        print(line.rstrip().replace('Python', 'JavaScript'))
print()

with open('learning_python.txt', encoding='UTF-8') as txt_file_object:
    txt_file_contents_as_list_of_lines = txt_file_object.readlines()
for line in txt_file_contents_as_list_of_lines:
    line = line.replace('Python', 'JavaScript')
    print(line.rstrip())
