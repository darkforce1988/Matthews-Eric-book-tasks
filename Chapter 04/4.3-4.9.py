kvadro = []
for number in range(1, 10):
    kvadro.append(number**2)
print(kvadro)
print(min(kvadro), max(kvadro), sum(kvadro))

kvadrati = [kvadrat**2 for kvadrat in range(1, 11)]
print(kvadrati)

summa = list(range(1, 1000001))
print(sum(summa))

kratnie = list(range(3, 31, 3))
print(kratnie)

kubi = []
for chislo in range(1, 11):
    kub = chislo**3
    kubi.append(kub)
    print(kub)
print(kubi)

kubiki = [kubik**3 for kubik in range(1, 11)]
print(kubiki)
