letter = str(input("Informe UMA letra: "))
vowels = str("aiueo")
consonants = False

if(len(letter) != 1):
    print("\nVocê digitou mais de uma letra, tente novamente!")

else:
    for i in vowels:
        if(letter.lower() == i):
            print("\nVocê digitou a vogal",letter.upper())
            consonants = True
    
    if(consonants == False):
        print("\nVocê digitou a consoante",letter.upper())
