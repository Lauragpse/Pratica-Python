valor_produto =  float (input())
desconto = float(input())

produto_desconto = (valor_produto * (desconto / 100))
desconto_total = (valor_produto - produto_desconto)

print ('%.2f' % valor_produto)
print ('%.2f' % desconto_total)
print ('%.2f' % produto_desconto)
