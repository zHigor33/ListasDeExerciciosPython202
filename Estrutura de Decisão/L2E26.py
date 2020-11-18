typeOfFuel = str(input("Escolha o tipo do combustivel:\nA- Alcool - G- Gasolina\n"))
numberOfLiters = int(input("\nQuantidade de litros desejada para abastecer: "))
total = float

if typeOfFuel == "A":
    if numberOfLiters <= 20:
        total = (numberOfLiters * 1.90) * 0.97
    
    else:
        total = (numberOfLiters * 1.90) * 0.95

elif typeOfFuel == "G":
    if numberOfLiters <= 20:
        total = (numberOfLiters * 2.50) * 0.96
    
    else:
        total = (numberOfLiters * 2.50) * 0.94

else:
    print("Opção Invalida!")

print("O total a pagar é de "+str(total))