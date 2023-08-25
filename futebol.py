time1 = str(input())
time2 = str(input())
gol_time1= int(input())
gol_time2 = int(input())

if gol_time1 > gol_time2:
  print('vitoria:', time1)
elif gol_time1 < gol_time2:
  print('vitoria:', time2)
elif gol_time1 == gol_time2:
  print('prorrogação!')
  print('disputa de penaltis!')
