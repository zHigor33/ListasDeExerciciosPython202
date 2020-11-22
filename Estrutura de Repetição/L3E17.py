i = int(input("Informe o número fatorial: "))
total = 1

for j in range(i):
    total = total * i
    i = i - 1

print("O resultado é "+str(total))
