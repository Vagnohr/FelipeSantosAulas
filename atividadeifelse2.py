#Faça um programa que receba uma nota do aluna e se for superior ou igual a 7 apareça mensagem que ele está aprovado, se for inferior a 5 ese está "não aprovado/reprovado direto" e se estiver entre 5 e 7 apareça mensagem "não aprovado/recuperação"
nota = int(input("Insira a nota: "))
if nota>=7:
    print("Aprovado")
if nota<5:
    print("Reprovado")
else:
    print("De recuperação")