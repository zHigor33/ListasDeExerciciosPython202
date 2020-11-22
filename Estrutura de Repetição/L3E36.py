multiplicationTable = int(input("Montar a tabuada de: "))
start = int(input("Começar por: "))
start -= 1
end = int(input("Terminar em: "))

print("\nVou montar a tabuada de "+str(multiplicationTable)+" começando em "+str(start + 1)+" e terminando em "+str(end)+":")

for i in range(start, end):
    start += 1
    total = multiplicationTable * start
    print(str(multiplicationTable)+" X "+str(start)+" = "+str(total))
