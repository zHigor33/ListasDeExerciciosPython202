firstSide = float(input("Informe o 1° lado do triangulo: "))
secondSide = float(input("Informe o 2° lado do triangulo: "))
thirdSide = float(input("Informe o 3° lado do triangulo: "))

triangleConfirmation = firstSide + secondSide

if triangleConfirmation < thirdSide:
    print("Não é um triângulo!")
    
else:
    if firstSide == secondSide == thirdSide:
        print("É um triângulo Equilátero")
        pass
    elif firstSide == secondSide != thirdSide:
        print("É um triângulo Isósceles")
        pass
    elif firstSide == thirdSide != secondSide:
        print("É um triângulo Isósceles")
        pass
    elif secondSide == thirdSide != firstSide:
        print("É um triângulo Isósceles")
        pass
    elif firstSide != secondSide != thirdSide:
        print("É um triângulo Escaleno") 
