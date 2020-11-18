firstValue = float(input("Informe o primeiro número: "))
secondValue = float(input("Informe o segundo número: "))
operation = str(input("Informe uma operação(+, -, /, *): "))
total = float
information = ""

if operation == "+":
    total = firstValue + secondValue

elif operation == "-":
    total = firstValue - secondValue

elif operation == "/":
    total = firstValue / secondValue

elif operation == "*":
    total = firstValue * secondValue

verifyTotal = round(total) - total

if total % 2:
    information = information + "\nImpar"

else:
    information = information + "\nPar"

if total > 0:
    information = information + "\nPositivo"

else:
    information = information + "\nNegativo"

if verifyTotal == 0:
    information = information + "\nInteiro"

else:
    information = information + "\nDecimal"

print("O resultado é "+str(total)+information)
