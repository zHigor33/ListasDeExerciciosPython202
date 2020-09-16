A = float(input("Informe o valor de A: "))
if A == 0:
    print("A é igual a zero, portanto não é uma equação de segundo gráu")

else:
    B = float(input("Informe o valor de B: "))
    C = float(input("Informe o valor de C: "))

    delta = B ** 2 - 4 * A * C

    if delta < 0:
        print("A equação não possui raizes reais!")
        pass
    elif delta == 0:
        X = -B + delta**(1/2) / (2*A)
        print("A equação possui apenas uma raiz, X=",X)
        pass
    else:
        X1 = -B + delta**(1/2) / (2*A)
        X2 = -B - delta**(1/2) / (2*A)
        print("A equação possui duas raizes, X1=",X1,"X2=",X2)
