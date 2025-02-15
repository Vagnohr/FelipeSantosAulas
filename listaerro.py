produtos=["tv","celular","tablet","mouse","teclado","geladeira","forno"]
procurar = input("Insira qual produtor deseja procurar: ")
if procurar not in produtos:
    print("Item não está na lista")
    procurar = input("Insira qual produtor deseja procurar: ")
elif procurar in produtos:
    i=produtos.index(procurar)
    print(produtos[i])