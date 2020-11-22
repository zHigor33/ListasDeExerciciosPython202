fatorial = int(input("Fatorial de: "))
printFatorial = fatorial
subtitleFatorial = str(fatorial) + "! = "
total = 1

for i in range(fatorial):
    total = total * fatorial
    fatorial -= 1

for i in range(printFatorial):
    subtitleFatorial = subtitleFatorial + str(printFatorial)

    if printFatorial > 1:
        subtitleFatorial = subtitleFatorial + " . "
    
    printFatorial -= 1

print(str(subtitleFatorial)+" = "+str(total))
