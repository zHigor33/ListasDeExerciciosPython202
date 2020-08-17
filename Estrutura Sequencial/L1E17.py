# 1 Litro para 6 metros quadrados
# 18 litros por lata a R$80,00
# 3,6 litros por latão a R$25,00
import math

area = float(input("Informe em metros quadrados a área a ser pintada: "))

# Quantidade de litros por metro quadrado
requiredInkPerLiter = math.ceil(float(area/6))

# Apenas latas
numberOfCans = math.ceil(float(requiredInkPerLiter/18))
pricePerCan = numberOfCans * 80

# Apenas galões
numberOfGallons = math.ceil(float(requiredInkPerLiter/3.6))
pricePerGallons = numberOfGallons * 25

# Latas e Galões
litersMargin = math.ceil(float(requiredInkPerLiter*1.1))
literOfCans = int(litersMargin/18)
percentageOfCans = litersMargin % 18
numberOfGallonsPerCan = math.ceil(percentageOfCans/3.6)
totalPrice = ((literOfCans*80) + (numberOfGallonsPerCan*25))

print("\n\nQuantidade de litros necessária é de ",requiredInkPerLiter,
        "\n\nO preço por cada opção é: ",
        "\nApenas latas R$",pricePerCan,"- Quantidade de latas",numberOfCans,
        "\nApenas galões R$",pricePerGallons,"- Quantidade de galões",numberOfGallons,
        "\nLatas e Galões R$",totalPrice,"- Quantidade de latas",literOfCans,"- Quantidade de galões",numberOfGallonsPerCan)