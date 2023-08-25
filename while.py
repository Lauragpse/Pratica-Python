minimo = int(input())
contador = 0

while contador < minimo:
    entrada=int(input())
    contador = contador+entrada

print('minimo', minimo)
print('total', contador)
print('sobra', contador-minimo)
