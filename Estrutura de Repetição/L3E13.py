base = int(input("Informe a base do número: "))
exponent = int(input("informe o expoente: "))
total = base

for i in range(exponent):
    base = base * total

base = base / total

print("O resultado da exponenciação é "+str(base))
