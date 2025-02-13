faturamento = input("Qual foi o faturamento da loja nesse mês? ")
custo = input("Qual foi o custo da loja nesse mês? ")
if faturamento == "" or custo == "":
    print("ERRO")
else:
    lucro = int(faturamento) - int(custo)
    print("O lucro da loja foi de {} R$".format(lucro))