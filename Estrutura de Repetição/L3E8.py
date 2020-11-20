verifyMedia = True
i = 1
sumOfNumbers = 0

while verifyMedia:
    numbers = float(input("Informe o "+str(i)+"° número: "))

    sumOfNumbers = sumOfNumbers + numbers
    i = i + 1

    if i == 6:
        verifyMedia = False

avarage = sumOfNumbers / (i - 1)

print("A média dos números é "+str(avarage)+" e a soma é "+str(sumOfNumbers))
