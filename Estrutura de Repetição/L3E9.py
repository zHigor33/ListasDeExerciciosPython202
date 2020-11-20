checkOddNumbers = True
i = 0
numbers = ""

while checkOddNumbers:
    if i % 2:
        numbers = numbers + "- " + str(i)
    
    i = i + 1

    if i == 50:
        checkOddNumbers = False

print("Os números impares de 1 a 50 são: "+numbers)
