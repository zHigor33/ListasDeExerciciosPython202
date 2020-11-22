amountOfPeople = int(input("Informe a quantidade de eleitores: "))
firstCandidate = 0
secondCandidate = 0
thirdCandidate = 0
nullVotes = 0

for i in range(amountOfPeople):
    wishes = int(input("Em quem você vota? Candidato 1, 2 ou 3: "))

    if wishes == 1:
        print("Você votou no primeiro candidato")
        firstCandidate += 1
    
    elif wishes == 2:
        print("Você votou no segundo candidato")
        secondCandidate += 1

    elif wishes == 3:
        print("Você votou no terceiro candidato")
        thirdCandidate += 1

    else:
        print("Você anulou o voto")
        nullVotes += 1

if firstCandidate > secondCandidate and firstCandidate > thirdCandidate:
    print("\nO primeiro candidato ganhou com "+str(firstCandidate)+" voto(s)\n"+str(nullVotes)+" pessoa(s) anularam")

elif secondCandidate > firstCandidate and secondCandidate > thirdCandidate:
    print("\nO segundo candidato ganhou com "+str(secondCandidate)+" voto(s)\n"+str(nullVotes)+" pessoa(s) anularam")

elif thirdCandidate > secondCandidate and thirdCandidate > firstCandidate:
    print("\nO terceiro candidato ganhou com "+str(thirdCandidate)+" voto(s)\n"+str(nullVotes)+" pessoa(s) anularam")

else:
    print("\nHouve um empate entre os candidatos")
