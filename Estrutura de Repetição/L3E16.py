loop = True
lastNumber = 1
firstNumber = 0

while loop:
    total = firstNumber + lastNumber
    lastNumber = firstNumber
    firstNumber = total

    if total >= 500:
        loop = False

    print(total)
