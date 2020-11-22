quantityOfCDs = int(input("Informe a quantidade de CDs: "))
sumOfCDs = 0

for i in range(quantityOfCDs):
    cds = int(input("Informe o valor do "+str(i + 1)+"° CD: "))

    sumOfCDs = sumOfCDs + cds

avarage = sumOfCDs / quantityOfCDs

print("\nO valor total gasto na coleção é de R$"+str(sumOfCDs)+"\nA média de preço dos CDs é de R$"+str(avarage))
