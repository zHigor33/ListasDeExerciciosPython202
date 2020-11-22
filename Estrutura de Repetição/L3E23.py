loop = True
number = int(input("Informe um número máximo que deseja saber o intervalo de números primos: "))
j = 1

while loop:
    checkList = 0
    splitList = []
    for i in range(j):
        if j % (i + 1) == 0:
            checkList = checkList + 1
            splitList.append(i + 1)
        
        else:
            checkList
    
    if checkList == 2 or checkList == 1:
        print("\n"+str(j)+" é um número primo pois é divisivel por "+str(splitList))

    else:
        print("\n"+str(j)+" não é um número primo pois é divisivel por "+str(splitList))

    j = j + 1

    if j > number:
        loop = False
