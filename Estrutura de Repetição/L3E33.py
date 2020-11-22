loop = True

while True:
    lowestTemperature = 0
    higherTemperature = 0
    avarage = 0
    total = 0
    i = 0
    quantityAvarage = 0

    print("Temperaturas\nPara terminar o registro basta informar uma temperatura de 99 ou maior\n")

    while loop:
        temperature = float(input("Informe a temperatura: "))
        quantityAvarage += 1

        if i == 0:
            lowestTemperature = temperature
            higherTemperature = temperature
            i += 1

        if temperature >= 99:
            loop = False
        
        else:
            if temperature < lowestTemperature:
                lowestTemperature = temperature
                total = total + temperature
            
            else:
                higherTemperature = temperature
                total = total + temperature
    
    avarage = total / quantityAvarage
    print("\nA maior temperatura é de "+str(higherTemperature)+"\nA menor temperatura é de "+str(lowestTemperature)+"\nA média das temperaturas é de "+str(avarage)+"\n")
    loop = True
