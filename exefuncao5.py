def get_data():
    nome_usuario=input("Escreva o seu nome: ")
    idade_usuario=int(input("QUal a sua idade? "))
    tupla_data=(nome_usuario, idade_usuario)
    return tupla_data
def mensagem(nome_usuario, idade_usuario):
    if idade_usuario<=10:
        print("Oi",nome_usuario)
    else:
        print("Olá!",nome_usuario)