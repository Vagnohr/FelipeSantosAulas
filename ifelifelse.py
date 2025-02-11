meta = int(input("Insira qual era a meta: "))
vendas = int(input("Insira a quantidade de vendas: "))

if vendas < meta:
    print("Não ganhou bônus")
elif vendas > (meta*2):
    print("Ganhou {} de bônus".format(bonus))
else:
    bonus = 0.03 * vendas
    print("Ganhou {} de bônus".format(bonus))