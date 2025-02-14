produtos=["tv","celular","tablet","mouse","teclado","geladeira","forno"]
item_usuario=input("Qual item deseja remover? ")
try:
    produtos.remove(item_usuario)
    print(produtos)
except:
    print("O produto {} não existe na lusta.".format(item_usuario))