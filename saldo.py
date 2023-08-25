limite = int(input())
gasto = int
itens = 0
saldo = limite

while saldo >= 0:
    gasto = int(input())
    if gasto > saldo:
        itens=itens+0
        saldo = saldo +0
        break
    else:
        itens +=1
        saldo = saldo-gasto

saldofloat = "%.2f" % saldo
    
print('Número de itens', itens)
print('Saldo:', saldofloat)
