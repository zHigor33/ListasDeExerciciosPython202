loop = True
listOfOddNumbers = 0
listOfEvenNumbers = 0
i = 1

while loop:
    numbers = int(input("Informe o "+str(i)+"° número: "))

    if numbers % 2:
        listOfOddNumbers = listOfOddNumbers + 1
    else:
        listOfEvenNumbers = listOfEvenNumbers + 1
    
    i = i + 1

    if i == 11:
        loop = False

print("\nExistem "+str(listOfEvenNumbers)+" números pares \nExistem "+str(listOfOddNumbers)+" números impares")
