def describe_sandwich(*components):
    print("The components of your sandwich:\n")
    for component in components:
        print(f"\t- {component}")
    print()


describe_sandwich('ketchup')

describe_sandwich('ketchup', 'ham')

describe_sandwich('ketchup', 'ham', 'egg', 'chicken meat')
