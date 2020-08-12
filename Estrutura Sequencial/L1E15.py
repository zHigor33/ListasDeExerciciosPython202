hourlyWage = float(input("Quanto você ganha por hora? "))
hour = float(input("Quantas horas trabalhou este mês? "))

salary = hourlyWage * hour
ir = salary / 100 * 11
inss = salary / 100 * 8
syndicate = salary / 100 * 5
netSalary = salary - ir - inss - syndicate

print(  "+ Salario Bruto : R$",salary,
        "\n- IR (11%) : R$",ir,
        "\n- INSS (8%) : R$",inss,
        "\n- Sindicato (5%) : R$",syndicate,
        "\n= Salario Liquido : R$",netSalary)
 