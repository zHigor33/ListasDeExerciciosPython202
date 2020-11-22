amountOfPeople = int(input("Informe a quantidade de pessoas da turma: "))
avarage = 0
sumOfAges = 0

for i in range(amountOfPeople):
    age = float(input("Informe a "+str(i + 1)+"° nota: "))
    sumOfAges = sumOfAges + age

avarage = sumOfAges / amountOfPeople

if avarage > 0 and avarage <= 25:
    print("A turma é Jovem!")

elif avarage > 25 and avarage < 60:
    print("A turma é Adulta!")

elif avarage >= 60:
    print("A turma é Idosa!")

else:
    print("As média das idades informadas são menor que 0!")
