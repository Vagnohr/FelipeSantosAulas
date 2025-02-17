vendas=[100,50,80,190,200,210,45,37,99,105,130,111,44,24,67,93,157,25]
meta =100
quantidade_bate_meta =0
for venda in vendas:
    if venda >= meta:
        print(venda)
        quantidade_bate_meta += 1
quantidade_funcionarios = len(vendas)
print("O porcentual de pessoas que bateram a meta foi de {:.1%}".format(quantidade_bate_meta/quantidade_funcionarios))