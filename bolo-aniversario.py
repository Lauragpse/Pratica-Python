velas = int(input())
fu = str
ano = velas
while velas > 0:
    fu = str(input())
    if fu == "fu":
        print("precisa de muito mais força no sopro!")
    elif fu == "fuuu":
        print("um pouco mais de força no sopro!")
    elif fu == "fuuuuuuu":
        print("bom sopro!")
        velas = velas - 1
print("Parabéns para pelo seu aniversário de", ano, "anos!")
