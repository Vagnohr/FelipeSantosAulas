clientes=["Felipe","Arthur","João","Gabriel"]
procurar = input("Insira qual cliente deseja procurar: ")
if procurar not in clientes:
    print("pessoa não está na lista")
    procurar = input("Insira qual cliente deseja procurar: ")
elif procurar in clientes:
    i=clientes.index(procurar)
    print(clientes[i])