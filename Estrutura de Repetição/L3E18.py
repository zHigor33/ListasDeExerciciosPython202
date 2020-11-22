loop = True
lowestNumber = 0
higherNumber = 0
total = 0
i = 0

while loop:
    numbers = float(input("Digite um número: "))

    if i == 0:
        lowestNumber = numbers
        higherNumber = numbers
        i = i + 1

    if lowestNumber > numbers:
        lowestNumber = numbers

    if higherNumber < numbers:
        higherNumber = numbers
    
    total = total + numbers

    breakLoop = str(input("Deseja informar mais números(s/n): "))

    if breakLoop == "s":
        print("Continue")

    elif breakLoop == "n":
        loop = False
    
    else:
        print("Informação errada, informe um número novamente!")

print("O menor número é "+str(lowestNumber)+"\nO maior número é "+str(higherNumber)+"\nA soma dos números é "+str(total))
