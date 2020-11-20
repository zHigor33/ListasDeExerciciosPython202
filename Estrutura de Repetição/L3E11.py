checkInterval = True
sumOfNumbers = 0

firstNumber = int(input("Informe o primeiro número: "))
secondNumber = int(input("Informe o segundo número: "))

if firstNumber > secondNumber:
    i = secondNumber
    lastNumber = firstNumber
else:
    i = firstNumber
    lastNumber = secondNumber

i = i + 1

while checkInterval:
    sumOfNumbers = sumOfNumbers + i

    i = i + 1

    if i == lastNumber:
        checkInterval = False

print("A soma do intervalo de números é "+str(sumOfNumbers))
