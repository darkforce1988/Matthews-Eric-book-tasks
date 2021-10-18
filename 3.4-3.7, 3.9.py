guests = ['pasiypa' , 'санька' , 'алик']
print(f"Привет, приходи на ужин, {guests[0].title()}.")
print(f"Привет, приходи на ужин, {guests[1].title()}.")
print(f"Привет, приходи на ужин, {guests[2].title()}.")
print(f"Однако, {guests[0].title()} не сможет прийти из-за диареи.")
guests[0] = 'костик'
print(f"Привет, приходи на ужин, {guests[0].title()}.")
print(f"Привет, приходи на ужин, {guests[1].title()}.")
print(f"Привет, приходи на ужин, {guests[2].title()}.")
guests.insert(0, "юрик")
guests.insert(1, "собака")
guests.append("Люба")
print(f"Привет, приходи на ужин, {guests[0].title()}.")
print(f"Привет, приходи на ужин, {guests[1].title()}.")
print(f"Привет, приходи на ужин, {guests[2].title()}.")
print(f"Привет, приходи на ужин, {guests[3].title()}.")
print(f"Привет, приходи на ужин, {guests[4].title()}.")
print(f"Привет, приходи на ужин, {guests[5].title()}.")
print("Упс, мы можем пригласить только двух гостей.")
while len(guests) > 2:
    minus = guests.pop(0)
    print(f"Извини, {minus}, я отменяю своё приглашение.")
print(f"Предложение насчёт ужина в силе, {guests[0].title()}.")
print(f"Предложение насчёт ужина в силе, {guests[1].title()}.")
del guests[0]
del guests[0]
print(guests)
