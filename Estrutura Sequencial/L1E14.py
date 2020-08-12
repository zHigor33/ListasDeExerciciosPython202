peso = float(input("Informe o peso em kg do peixe: "))

if(peso > 50):
    excesso = peso - 50
    multa = excesso * 4
    print("Peso limite excedeu, a multa é de R$",multa)

else:
    print("Peso dentro do limite, sem multa!")
