def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File '{filename}' is not found.")
    else:
        count = contents.lower().count('the')
        print(f"Number of 'the' in book '{filename}' is: {count}.")
        count = contents.lower().count('the ')
        print(f"Number of 'the ' in book '{filename}' is: {count}.")


filenames = ['Ancient Rome and Modern America.txt', 'Broken Barriers.txt']
for filename in filenames:
    count_words(filename)
