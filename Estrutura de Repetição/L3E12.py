checkMultiplicationTable = True
informTheMultiplicationTable = int(input("Informe a tabuada que deseja ver: "))
i = 1

print("Tabuada de "+str(informTheMultiplicationTable)+" é:")
while checkMultiplicationTable:
    printMultiplicationTable = informTheMultiplicationTable * i

    print(str(informTheMultiplicationTable)+" X "+str(i)+" = "+str(printMultiplicationTable))

    i = i + 1

    if i == 11:
        checkMultiplicationTable = False
