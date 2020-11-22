numberOfNumbers = int(input("Quantos numeros deseja informar: "))
lowestNumber = 0
higherNumber = 0
total = 0

for i in range(numberOfNumbers):
    loop = True

    while loop:
        numbers = float(input("Informe o número: "))

        if numbers >= 0 and numbers <= 1000:
            loop = False
        
        else:
            print("O número informado passa de 1000 ou é menor que 0")
    
    if i == 0:
        lowestNumber = numbers
        higherNumber = numbers
    
    if lowestNumber > numbers:
        lowestNumber = numbers

    if higherNumber < numbers:
        higherNumber = numbers
    
    total = total + numbers

print("O menor número é "+str(lowestNumber)+"\nO maior número é "+str(higherNumber)+"\nA soma dos números é "+str(total))
