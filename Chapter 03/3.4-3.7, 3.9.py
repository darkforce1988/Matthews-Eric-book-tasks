guests = ['paSiYupa', 'санька', 'алик']
for i in range(0, len(guests)):
    guests[i] = guests[i].title()

for guest in guests:
    print(f"Привет, приходи на ужин, {guest}.")
print("\nВы все красавчики\n")

print(f"Однако, {guests[0]} не сможет прийти из-за диареи.")

guests[0] = 'костик'.title()
print(f"Привет, приходи на ужин, {guests[0]}.")
print(f"Привет, приходи на ужин, {guests[1]}.")
print(f"Привет, приходи на ужин, {guests[2]}.")

guests.insert(0, "юрик".title())
guests.insert(1, "собака".title())
guests.append("люба".title())
print(f"Привет, приходи на ужин, {guests[0]}.")
print(f"Привет, приходи на ужин, {guests[1]}.")
print(f"Привет, приходи на ужин, {guests[2]}.")
print(f"Привет, приходи на ужин, {guests[3]}.")
print(f"Привет, приходи на ужин, {guests[4]}.")
print(f"Привет, приходи на ужин, {guests[5]}.")

print("Упс, мы можем пригласить только двух гостей.")
print(f"{guests.pop()}, пошёл нафиг, мы больше не друзья!")
print(f"{guests.pop()}, пошёл нафиг, мы больше не друзья!")
print(f"{guests.pop()}, пошёл нафиг, мы больше не друзья!")
print(f"{guests.pop()}, пошёл нафиг, мы больше не друзья!")

print(f"Предложение насчёт ужина в силе, {guests[0]}.")
print(f"Предложение насчёт ужина в силе, {guests[1]}.")

print("Количество приглашённых людей на ужин - " + str(len(guests)))

print(sorted(guests))

guests.reverse()
print(guests)

del guests[0]
del guests[0]
print(guests)
