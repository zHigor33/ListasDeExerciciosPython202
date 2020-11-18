print("                   Até 5 Kg       Acima de 5 Kg")
print("File Duplo   R$ 4,90 por Kg      R$ 5,80 por Kg")
print("Alcatra      R$ 5,90 por Kg      R$ 6,80 por Kg")
print("Picanha      R$ 6,90 por Kg      R$ 7,80 por Kg")

typeOfMeat = str(input("Informe o tipo de carne (file/alcatra/picanha): "))
quantityInKilos = float(input("Informe o peso em quilos: "))
cardTabajara = str(input("Vai pagar com o cartão Tabajara (s/n): "))

if typeOfMeat == "file":
    if quantityInKilos <= 5:
        total = quantityInKilos * 4.9
    
    elif quantityInKilos > 5:
        total = quantityInKilos * 5.8

elif typeOfMeat == "alcatra":
    if quantityInKilos <= 5:
        total = quantityInKilos * 5.9
    
    elif quantityInKilos > 5:
        total = quantityInKilos * 6.8

elif typeOfMeat == "picanha":
    if quantityInKilos <= 5:
        total = quantityInKilos * 6.9
    
    elif quantityInKilos > 5:
        total = quantityInKilos * 7.8

else:
    print("Carne não existente!")

if cardTabajara == "s":
    totalWithDiscount = total * 0.95

    print("\n                  Nota Fiscal:              ")
    print("Tipo de carne:                "+str(typeOfMeat))
    print("Quantidade (Kg):              "+str(quantityInKilos))
    print("Preço total:                  "+str(total))
    print("Tipo de pagamento:            Cartão Tabajara")
    print("Valor a pagar (com desconto): "+str(totalWithDiscount))
