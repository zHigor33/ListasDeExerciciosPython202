print("                   Até 5 Kg       Acima de 5 Kg")
print("Morango      R$ 2,50 por Kg      R$ 2,20 por Kg")
print("Maçã         R$ 1,80 por Kg      R$ 1,50 por Kg")

typeOfFruit = str(input("\nInforme a fruta que irá comprar (morango/maca): "))
quantityInKilos = int(input("Informe o peso em quilos: "))

if typeOfFruit == "morango":
    if quantityInKilos <= 5:
        total = quantityInKilos * 2.50
    
    elif quantityInKilos > 5:
        total = quantityInKilos * 2.20
    
    if total > 25:
        total = total * 0.9

elif typeOfFruit == "maca":
    if quantityInKilos <= 5:
        total = quantityInKilos * 1.80
    
    elif quantityInKilos > 5:
        total = quantityInKilos * 1.50
    
    if total > 25:
        total = total * 0.9

else:
    print("Fruta não cadastrada!")

print("O total a pagar é de R$"+str(total)+"\nQuantidade em quilos foi de "+str(quantityInKilos))
