# Arquivo em MB (1 gb é 1024mb)
# Velocidade em Mbps (MegaBits por Segundo)
# Calcular o tempo e mostrar em minutos

fileSize = float(input("Informe o tamanho do arquivo em MB: "))
downloadSpeed = float(input("Informe a velocidade de download em Mbps: "))

timePerSecond = fileSize / downloadSpeed
timePerMinutes = timePerSecond / 60

print("O tempo do Download será de %d segundos" % (timePerSecond))
print("O tempo do Download será de %d minuto(s)" % (timePerMinutes))
