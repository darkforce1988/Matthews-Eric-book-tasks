filenames = ['Ancient Rome and Modern America.txt', 'Broken Barriers.txt']
for filename in filenames:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        count = contents.lower().count('the')
        print(f"Number of 'the' in book '{filename}' is: {count}.")
        count = contents.lower().count('the ')
        print(f"Number of 'the ' in book '{filename}' is: {count}.")
