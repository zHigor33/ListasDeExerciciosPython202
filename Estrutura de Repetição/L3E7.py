verifyNumber = True
i = 1
higherNumber = 0

while verifyNumber:

    infoNumber = float(input("Informe o "+str(i)+"° número: "))

    if infoNumber > higherNumber:
        higherNumber = infoNumber
    
    i = i + 1

    if i == 6:
        verifyNumber = False

print("O maior número informado foi o "+str(higherNumber))
