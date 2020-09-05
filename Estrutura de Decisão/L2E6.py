numberOne = float(input("Informe o 1° número: ")); 
numberTwo = float(input("Informe o 2° número: ")); 
numberThree = float(input("Informe o 3° número: ")); 

if(numberOne >= numberTwo >= numberThree):
    print("O número %d é o maior!" % (numberOne))

elif(numberTwo >= numberThree >= numberOne):
    print("O número %d é o maior!" % (numberTwo))

elif(numberThree >= numberTwo >= numberOne):
    print("O número %d é o maior!" % (numberThree))