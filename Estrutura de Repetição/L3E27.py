loopOfStudents = True
numberOfClasses = int(input("Informe a quantidade de turmas: "))
sumOfStudents = 0

for i in range(numberOfClasses):
    while loopOfStudents:
        numberOfStudents = int(input("Informe a quantidade de alunos da turma "+str(i + 1)+": "))

        if numberOfStudents <= 40:
            loopOfStudents = False
        
        else:
            print("A quantidade de alunos se excedeu, informe novamente!")
        
    sumOfStudents = sumOfStudents + numberOfStudents
    loopOfStudents = True

avarage = sumOfStudents / numberOfClasses

print("A média de alunos por turma é de "+str(avarage))
