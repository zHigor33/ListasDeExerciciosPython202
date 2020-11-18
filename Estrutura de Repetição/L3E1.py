verifyValue = True

while verifyValue:
    value = int(input("Informe um valor entre 0 e 10: "))

    if value > 0 and value < 10:
        print("Valor valido")
        verifyValue = False
    
    else:
        print("Valor invalido")
