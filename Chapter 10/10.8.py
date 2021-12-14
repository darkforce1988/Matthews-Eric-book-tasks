filenames = ['cats.txt', 'dogs.txt', 'rabbits.txt']

for filename in filenames:
    try:
        with open(filename, encoding='UTF-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} is not found.")
    else:
        print(contents)
