filenames = ['cats.txt', 'dogs.txt', 'rabbits.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"File {filename} is not found.")
