firstProduct = float(input("Informe o preço do 1° produto: R$"))
secondProduct = float(input("Informe o preço do 2° produto: R$"))
thirdProduct = float(input("Informe o preço do 3° produto: R$"))

if(firstProduct <= secondProduct <= thirdProduct):
    print("Voce deve comprar o 1° produto porque é mais barato!")

elif(secondProduct <= thirdProduct <= firstProduct):
    print("Voce deve comprar o 1° produto porque é mais barato!")

elif(thirdProduct <= secondProduct <= firstProduct):
        print("Voce deve comprar o 1° produto porque é mais barato!")
