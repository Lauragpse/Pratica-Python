objeto = str(input())
lista = str(input()).split()

if objeto in lista:
    resultado = lista.index(objeto)
    print(objeto, resultado)
else:
    print('falta', objeto)
