firstQuestion = str(input("Telefonou para a vítima?"))
secondQuestion = str(input("Esteve no local do crime?"))
thirdQuestion = str(input("Mora perto da vítima?"))
fourthQuestion = str(input("Devia para a vítima?"))
fifthQuestion = str(input("Já trabalhou com a vítima?"))

if fifthQuestion == "sim":
    print("Assassino")

elif thirdQuestion == "sim" or fourthQuestion == "sim":
    print("Cúmplice")

elif secondQuestion == "sim":
    print("Suspeita")

else:
    print("Inocente")
