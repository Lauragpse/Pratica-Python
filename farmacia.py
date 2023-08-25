atual = [int(i) for i in input ().split()]
vencido= [int(i) for i in input().split()]
if vencido[2] > atual [2]:
     print("na validade")
elif vencido [1] > atual[1]:
    print("vence este ano")
elif vencido [1] == atual [1] and vencido [0] >= atual [0]:
    print("vence este mês")
else:
    print("vencido!")
