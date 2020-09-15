turn = str(input("Informe seu turno de estudo (M/v/n): "))

if turn.lower() == "m":
    print("Bom dia")
    pass
elif turn.lower() == "v":
    print("Boa tarde")
    pass
elif turn.lower() == "n":
    print("Boa noite")
    pass
else:
    print("Opção invalida")
