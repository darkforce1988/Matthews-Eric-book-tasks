def sandwich_describe(*components):
    print("The components of your sandwich:\n\t")
    for component in components:
        print(f"- {component}")


sandwich_describe('ketchup')

print()
sandwich_describe('ketchup', 'ham')

print()
sandwich_describe('ketchup', 'ham', 'egg', 'chicken meat')
