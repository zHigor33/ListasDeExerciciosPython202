numberOfRatings = int(input("Informe o número de avaliações: "))
avarage = 0
sumOfRatings = 0

for i in range(numberOfRatings):
    assessments = float(input("Informe a "+str(i + 1)+"° nota: "))
    sumOfRatings = sumOfRatings + assessments

avarage = sumOfRatings / numberOfRatings

print("\nA média das "+str(numberOfRatings)+" notas é de "+str(avarage))
