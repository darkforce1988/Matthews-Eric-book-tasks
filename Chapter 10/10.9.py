filenames = ['rabbits.txt', 'cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename, encoding='UTF-8') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass
