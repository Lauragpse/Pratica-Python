palavra = str( input())
soletrando = str( input())
counting = ''
while soletrando != '.':
    counting = counting + soletrando
    soletrando = str( input())
if counting == palavra:
    print('True')
else:
    print('False')

