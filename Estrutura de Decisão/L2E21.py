bankValue = int(input("Digite o valor que deseja sacar(Máximo R$600,00): "))
total = bankValue
verifyWhile = True
hundredBucks = 0
fiftyBucks = 0
tenBucks = 0
fiveBucks = 0
oneBucks = 0

while verifyWhile == True:
    if bankValue >= 100:
        bankValue = bankValue - 100
        hundredBucks = hundredBucks + 1       

    elif bankValue >= 50:
        bankValue = bankValue - 50
        fiftyBucks = fiftyBucks + 1
        
    elif bankValue >= 10:
        bankValue = bankValue - 10
        tenBucks = tenBucks + 1

    elif bankValue >= 5:
        bankValue = bankValue - 5
        fiveBucks = fiveBucks + 1
        
    elif bankValue >= 1:
        bankValue = bankValue - 1
        oneBucks = oneBucks + 1
        
    elif bankValue == 0:
        verifyWhile = False
        

print("\nPara o valor de R$%d,00 foi usado %d notas de R$100, %d notas de R$50, %d notas de R$10, %d notas de R$5, %d notas de R$1" % (total, hundredBucks, fiftyBucks, tenBucks, fiveBucks, oneBucks))
