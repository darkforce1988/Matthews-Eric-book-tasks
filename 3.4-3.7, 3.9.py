guests = ['paSiYupa', 'санька', 'алик']
for i in range(0, len(guests)):
    guests[i] = guests[i].title()

print(f"Привет, приходи на ужин, {guests[0]}.")
print(f"Привет, приходи на ужин, {guests[1]}.")
print(f"Привет, приходи на ужин, {guests[2]}.")

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
while len(guests) > 2:
    minus = guests.pop(0)
    print(f"Извини, {minus}, я отменяю своё приглашение.")

print(f"Предложение насчёт ужина в силе, {guests[0]}.")
print(f"Предложение насчёт ужина в силе, {guests[1]}.")

print("Количество приглашённых людей на ужин - " + str(len(guests)))
print(sorted(guests))

guests.reverse()
print(guests)

while len(guests) > 0:
    del guests[0]
print(guests)
