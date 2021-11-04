ppl_for_vote = ['jen', 'sarah', 'edward', 'phil', 'paciupa', 'sarah']
people_already_voted = []
for ppl in ppl_for_vote:
    if ppl not in people_already_voted:
        print(f"{ppl.title()}, do you wanna take part in voting?")
        people_already_voted.append(ppl)   
    else:
        print(f"{ppl.title()}, thanks for your vote!")
