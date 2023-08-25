carta1 = input()
carta2 = input()
carta3 = input()
contador = 0

cartas = [carta1, carta2, carta3]
manilha = ('4Paus', '7Copas', 'AEspadas', '7Ouros')
for item in cartas:
    if item in manilha:
        contador += 1
print(contador)
