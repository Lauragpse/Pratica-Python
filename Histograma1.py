lista = [int(i) for i in input().split()]
for i in lista:
    linha = ''
    if i %2 == 0:
        for j in range(i):
            linha += '*'
    else:
        for j in range(i):
            linha += '.'
    print(linha)
