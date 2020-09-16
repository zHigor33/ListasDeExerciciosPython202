number = str(input("Informe um número menor que 1000: "))
hundred = 0
ten = 0
unit = 0

if int(number) < 1000:
    if int(number) > 100:
        hundred = number[0]
        ten = number[1]
        unit = number[2]
    
    elif int(number) < 100 and int(number) > 9:
        ten = number[0]
        unit = number[1]
    
    elif int(number) < 10:
        unit = number[1]

    print(number+" = "+hundred+" centena(s) "+ten+" dezena(s) "+unit+" unidade(s)")
else:
    print("O número informado é maior que mil")
