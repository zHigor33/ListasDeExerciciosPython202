loop = True
loopForI = True
total = 1

while loop:
    while loopForI:
        i = int(input("Informe o número fatorial: "))

        if i > 0 and i < 16 and i:
            loopForI = False
        
        else:
            print("O valor informado é invalido, informe novamente!")

    for j in range(i):
        total = total * i
        i = i - 1

    print("O resultado é "+str(total))
    recalculate = str(input("Deseja realizar outro calculo(s/n): "))

    if recalculate == "n":
        loop = False
    
    else:
        loopForI = True
