vendas_tecnologia={"iphone":15000,"sansung galaxy":12000,"Tv Samsung":10000,"ps5":14300,"tabelt":1720,"ipad":1200}
#for chave in vendas_tecnologia:
    #print("O produto {} vendeu {} unidades.".format(chave,vendas_tecnologia(chave)))
#for item in vendas_tecnologia.items():
    #print(item)
for produto, vendas in vendas_tecnologia.items():
    print("{}: {} de unidades.".format(produto,vendas))