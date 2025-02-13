produtos=["tv","celular","tablet","mouse","teclado","geladeira","forno"]
estoque=[100,150,100,120,70,180,80]
produto=input("Insira o nome do produto em letra minuscula: ")
if produto not in produtos:
    print("Produto não registrado")
else:
    i=produtos.index(produto)
    print(str(produtos[i]))
    print(str(estoque[i]))