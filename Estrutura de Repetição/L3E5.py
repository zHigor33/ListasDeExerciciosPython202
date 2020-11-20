verifyInformation = True
count = 0

while verifyInformation:
    cityA = int(input("Informe a quantidade de habitantes da cidade A: "))
    cityB = int(input("Informe a quantidade de habitantes da cidade B: "))

    if cityA < cityB:
        growhRateA = float(input("Informe a taxa de crescimento da cidade A (1= 100%/ 1.5= 50%):"))
        growhRateB = float(input("Informe a taxa de crescimento da cidade B (1= 100%/ 1.5= 50%):"))

        if growhRateA > growhRateB:
            calculation = True
            
            while calculation:
                cityA = cityA * growhRateA
                cityB = cityB * growhRateB
                count = count + 1

                if cityA >= cityB:
                    print("Precisa de "+str(count)+" anos para a cidade A se igualar a cidade B")
                    calculation = False
                    verifyInformation = False

        else:
            print("A taxa de crescimento de A não pode ser menor que B")

    else:
        print("A quantidade de habitantes de A não pode ser maior que B")
