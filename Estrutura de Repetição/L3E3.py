verifyInfo = True

while verifyInfo:
    name = str(input("Informe um nome: "))
    age = int(input("Informe sua idade: "))
    salary = float(input("Informe seu salario: "))
    sex = str(input("Informe seu sexo (m/f): "))
    maritalStatus = str(input("Informe seu estado civil (s/c/v/d): "))

    quantityOfCaracters = len(name)

    if quantityOfCaracters > 3:
        if age > 0 and age < 150:
            if salary > 0:
                if sex == "m" or sex == "f":
                    if maritalStatus == "s" or maritalStatus == "c" or maritalStatus == "v" or maritalStatus == "d":
                        print("Informações validas")
                        verifyInfo = False
                    
                    else:
                        print("Estado civil invalido")

                else:
                    print("Sexo invalido")

            else:
                print("Salario invalido")

        else:
            print("Idade invalida")
    
    else:
        print("Nome invalido")
