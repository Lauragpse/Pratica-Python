print('coloque uma temperatura em celsius para ser convertida em fahrenheit:')
temperaturacelsius = int(input('temperatura Celsius:' )) 
calculo = (temperaturacelsius * 9/5) + 32
resultado = "A temperatura em fahrenheit é: " + str(calculo)
print(resultado)

print('coloque uma temperatura em celsius para ser convertida em kelvin:')
temperaturacelsius = int(input('temperatura Celsius:' ))
calculo = (temperaturacelsius + 273.15)
resultado = "A temperatura em Kelvin é: " + str(calculo) 
print(resultado)
