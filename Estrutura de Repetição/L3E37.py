loop = True
i = 0
j = 0

lowestWeight = 0
higherWeight = 0

lowestHeight = 0
higherHeight = 0

totalWeight = 0
totalHeight = 0

lowestWeightLegend = ""
higherWeightLegend = ""

lowestHeightLegend = ""
higherHeightLegend = ""

while loop:
    code = int(input("Informe o código do cliente: "))

    if code == 0:
        loop = False
        avarageWeight = totalWeight / j
        avarageHeight = totalHeight / j

    else:
        weight = int(input("Informe o peso do cliente "+str(code)+": "))
        height = int(input("Informe a altura do cliente "+str(code)+": "))

        totalWeight = totalWeight + weight
        totalHeight = totalHeight + height

        if i == 0:
            lowestWeight = weight
            higherWeight = weight

            lowestHeight = height
            higherHeight = height

            i += 1
        
        if weight <= lowestWeight:
            lowestWeight = weight
            lowestWeightLegend = "O cliente de código " + str(code) + " é o mais magro"

        if weight >= higherWeight:
            higherWeight = weight
            higherWeightLegend = "O cliente de código " + str(code) + " é o mais gordo"

        if height <= lowestHeight:
            lowestHeight = height
            lowestHeightLegend = "O cliente de código " + str(code) + " é o mais baixo"

        if height >= higherHeight:
            higherHeight = height
            higherHeightLegend = "O cliente de código " + str(code) + " é o mais alto"
        
        j += 1

print("\nA média das alturas dos clientes é de "+str(avarageHeight))
print("A média dos pesos dos clientes é de "+str(avarageWeight))
print(lowestWeightLegend)
print(higherWeightLegend)
print(lowestHeightLegend)
print(higherHeightLegend)
