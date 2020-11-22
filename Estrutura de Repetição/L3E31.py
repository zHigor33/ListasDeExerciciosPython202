loop = True

while True:
    print("\nLojas Tabajara")
    i = 1
    total = 0

    while loop:
        product = float(input("Produto "+str(i)+": R$ "))
        total = total + product
        i += 1

        if product == 0:
            loop = False
    
    print("Total: R$ "+str(total))
    money = float(input("Dinheiro: R$ "))
    print("Troco: R$ "+str(money - total))
    loop = True
