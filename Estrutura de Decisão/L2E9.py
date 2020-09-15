numberOne = float(input("Informe o 1° número: ")); 
numberTwo = float(input("Informe o 2° número: ")); 
numberThree = float(input("Informe o 3° número: ")); 

if(numberOne >= numberTwo >= numberThree):
    print("%d - %d - %d" % (numberThree, numberTwo, numberOne))

elif(numberTwo >= numberThree >= numberOne):
    print("%d - %d - %d" % (numberOne, numberThree, numberTwo))

elif(numberThree >= numberTwo >= numberOne):
    print("%d - %d - %d" % (numberOne, numberTwo, numberThree))

elif(numberTwo >= numberOne >= numberThree):
    print("%d - %d - %d" % (numberThree, numberOne, numberTwo))
