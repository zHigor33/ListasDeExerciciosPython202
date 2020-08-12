manOrWoman = str(input("Você é home ou mulher?(H/m) "))

if(manOrWoman.lower() == "h"):
    height = float(input("Informe sua altura: "))
    print("Seu peso ideal é",(72.7*height)-58)

elif(manOrWoman.lower() == "m"):
    height = float(input("Informe sua altura: "))
    print("Seu peso ideal é",(62.1*height)-44.7)

else:
    print("Opção errada, tente novamente!")
