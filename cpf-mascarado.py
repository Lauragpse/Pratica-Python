cpf = input()
txt =  ""
for i in cpf:
  if int(i) % 2 ==0:
    txt += "*"
  else:
    txt += i


print(txt)
