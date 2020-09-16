firstGrade = float(input("Informe a primeira nota: "))
secondGrade = float(input("Informe a segunda nota: "))
thirdGrade = float(input("Informe a terceira nota: "))

average = (firstGrade + secondGrade + thirdGrade) / 3

if average == 10:
    print("Aprovado com distinção, média ",average)
elif average < 10 and average >= 7:
    print("Aprovado, média ",average)
elif average < 7:
    print("Reprovado, média ",average)
else:
    print("Existe média maior que dez?! média ",average)
