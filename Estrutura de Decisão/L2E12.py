hourlyValue = float(input("Informe o valor por hora: R$"))
hourPerMouth = float(input("Informe as horas trabalhadas no mês: "))

salary = hourlyValue * hourPerMouth
totalDiscount = float
ir = int
fgts = 0.11
inss = 0.1
discount = float
percent = float

if salary <= 900:
    ir = 0
    inss = inss * salary
    fgts = fgts * salary
    discount = inss
    percent = 0
    liquidSalary = salary - discount
    pass

elif salary > 900 and salary <= 1500:
    ir = 0.05 * salary
    inss = inss * salary
    fgts = fgts * salary
    discount = ir + inss
    percent = 5
    liquidSalary = salary - discount
    pass

elif salary > 1500 and salary <= 2500:
    ir = 0.1 * salary
    inss = inss * salary
    fgts = fgts * salary
    discount = ir + inss
    percent = 10
    liquidSalary = salary - discount
    pass

elif salary >  2500:
    ir = 0.2 * salary
    inss = inss * salary
    fgts = fgts * salary
    discount = ir + inss
    percent = 20
    liquidSalary = salary - discount
    pass

print("Salário bruto:       R$%d" % (salary))
print("IR(%d):               R$%d" % (percent, ir))
print("INSS(10):            R$%d" % (inss))
print("FGTS(11):            R$%d" % (fgts))
print("Total de desconto:   R$%d" % (discount))
print("Salário líquido:     R$%d" % (liquidSalary))
