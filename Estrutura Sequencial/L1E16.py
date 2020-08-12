squareMeter = float(input("Informe a área em metros quadrados a ser pintada: "))

liters = squareMeter / 3
pricePerCan = liters * 4.45
cans = liters / 18

print("Para pintar a área será necessário",cans,"lata(s) e vai custar R$",pricePerCan)
