valor = int(input())
aleatorio = int
while valor > 0:
    aleatorio = int(input())
    if valor > aleatorio:
        print('maior')
        aleatorio = aleatorio+1
    elif valor < aleatorio:
        print('menor')
        aleatorio = aleatorio+1
    elif valor == aleatorio:
        print('igual')
        break
