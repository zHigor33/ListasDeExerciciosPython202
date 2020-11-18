verify = True
cityA = 80000
cityB = 200000
count = 0

while verify:
    cityA = cityA * 1.03
    cityB = cityB * 1.015

    count = count + 1

    if cityA >= cityB:
        print("Precisa de "+str(count)+" anos para a cidade A se igualar a cidade B")
        verify = False
    
    else: continue
