checkInterval = True
intervalOfNumbers = ""

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
    intervalOfNumbers = intervalOfNumbers + " - " + str(i)

    i = i + 1

    if i == lastNumber:
        checkInterval = False

print("O intervalo de números entre "+str(firstNumber)+" e "+str(secondNumber)+" é"+intervalOfNumbers)
