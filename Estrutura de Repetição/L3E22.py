number = int(input("Informe um número que deseja saber se é primo: "))
splitList = []
checkList = 0

for i in range(number):
    if number % (i + 1) == 0:
        checkList = checkList + 1
        splitList.append(i + 1)
    
    else:
        checkList = checkList + 1

if checkList == 2:
    print("É um número primo pois é divisivel por "+str(splitList))

else:
    print("Não é um número primo pois é divisivel por "+str(splitList))
