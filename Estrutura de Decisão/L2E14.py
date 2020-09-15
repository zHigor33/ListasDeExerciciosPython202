firstNote = float(input("Informe a primeira nota parcial: "))
secondNote = float(input("Informe a segunda nota parcial: "))

media = (firstNote + secondNote) / 2
result = str

if media >= 9 and media <= 10:
    result = "A"
    pass
elif media >= 7.5 and media < 9:
    result = "B"
    pass
elif media >= 6 and media < 7.5:
    result = "C"
    pass
elif media >= 4 and media < 6:
    result = "D"
    pass
elif media < 4:
    result = "E"
    pass

if result == "D" or result == "E":
    print("REPROVADO, conceito",result)
    pass
else:
    print("APROVADO, conceito",result)
