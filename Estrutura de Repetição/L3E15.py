fibonacciSize = int(input("Informe a quantidade de números de Fibonacci que deseja: "))
i = 1
lastNumber = 1
firstNumber = 0

for i in range(fibonacciSize):
    total = firstNumber + lastNumber
    lastNumber = firstNumber
    firstNumber = total
    print(total)
