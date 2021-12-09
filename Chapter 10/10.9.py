filenames = ['rabbits.txt', 'cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass
