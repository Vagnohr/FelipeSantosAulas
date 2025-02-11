#Faça um programa que o ususario digite um número e diga se o numero é superior a 20. inferior a 10 ou se está entre 10 e 20
num = int(input("Insira um número: "))
if num>20:
    print("O número é superior a 20")
elif num<10:
    print("O número é inferior a 10")
else:
    print("O número está entre 10 e 20")