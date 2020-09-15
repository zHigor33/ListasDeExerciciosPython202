salary = float(input("Bem-vindo a Tabajara! \n\n Informe seu sálario: "))
reajustment = float
salaryDifferential = float
percent = float

if salary <= 280:
    reajustment = salary * 1.2
    percent = 20
    pass

elif salary > 280 and salary <= 700:
    reajustment = salary * 1.15
    percent = 15
    pass

elif salary > 700 and salary <= 1500:
    reajustment = salary * 1.1
    percent = 10
    pass

elif salary > 1500:
    reajustment = salary *1.05
    percent = 5
    pass

salaryDifferential = reajustment - salary

print("Salário atual:          R$%d \nPercentual aumentado:   %d porcento \nValor do aumento:       R$%d \nNovo salário:           R$%d" % (salary, percent, salaryDifferential,reajustment))
