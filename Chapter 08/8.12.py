def sandwich_describe(*components):
    print("The components of your sandwich:\n")
    for component in components:
        print(f"\t- {component}")
    print()


sandwich_describe('ketchup')

sandwich_describe('ketchup', 'ham')

sandwich_describe('ketchup', 'ham', 'egg', 'chicken meat')
