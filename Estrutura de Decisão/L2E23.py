value = float(input("Informe um número: "))
verifyValue = round(value)

if value - verifyValue == 0:
    print("Número inteiro")

else: 
    print("Número decimal")
