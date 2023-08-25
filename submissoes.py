problema = int(input())
teste = ""
nsubm = 0
aceito = 0
while problema > 0:
  teste = input()
  if teste == "accepted":
    problema -= 1
    nsubm += 1
    aceito += 1
  elif teste == "error":
    nsubm +=1
  elif teste == "timeout":
    break

print("submissoes: ",nsubm)
print("aceitos: ",aceito)
