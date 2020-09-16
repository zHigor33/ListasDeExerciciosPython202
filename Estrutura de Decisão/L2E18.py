dateDay = int(input("Informe o dia: "))
dateMonth = int(input("Informe o mês: "))
dateYear = int(input("Informe o ano: "))

date = ""

if dateDay <= 31:
    if dateMonth <= 12:
        if dateMonth == 2 and dateDay <= 29:
            if dateYear % 4 == 0 and dateDay <= 29:
                date = str(dateDay) + "/" + str(dateMonth) + "/" + str(dateYear)
                print("A data digitada foi: "+date)
                pass

            elif dateYear % 4 != 0 and dateDay <= 28:
                date = str(dateDay) + "/" + str(dateMonth) + "/" + str(dateYear)
                print("A data digitada foi: "+date)
                pass

            else:
                print("Data Inválida")
                pass

        elif (dateDay <= 31) and dateMonth == 1 or dateMonth == 3 or dateMonth == 5 or dateMonth == 7 or dateMonth == 8 or dateMonth == 12:
            date = str(dateDay) + "/" + str(dateMonth) + "/" + str(dateYear)
            print("A data digitada foi: "+date)
            pass

        elif (dateDay <= 30) and dateMonth == 4 or dateMonth == 6 or dateMonth == 9 or dateMonth == 11:
            date = str(dateDay) + "/" + str(dateMonth) + "/" + str(dateYear)
            print("A data digitada foi: "+date)
            pass

        else:
            print("Dia Inválida")
    else:
        print("Mês Inválido")
else:
    print("Dia Inválida")
