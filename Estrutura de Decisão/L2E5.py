firstGrade = float(input("Informe a primeira nota: "))
secondGrade = float(input("Informe a segunda nota: "))

average = (firstGrade + secondGrade) / 2

if(average >= 7):
    if(average == 10):
        print("\nAluno Aprovado com Distinção! Nota",average)

    else:    
        print("\nAluno Aprovado! Nota",average)
    
elif(average < 7):
    print("\nAluno Reprovado! Nota",average)
