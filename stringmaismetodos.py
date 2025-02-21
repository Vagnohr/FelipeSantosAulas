#transforma apenas a primeira letra de uma string em maiuscula
nome = "felipe"
print(nome.capitalize(),"\n")


#transforma todas as letras em minuscula
nome = "FELIPE"
print(nome.casefold(), "\n")


#conta o numero de vezes que um caractere specifico aparece na string
nome = "felipebtst1@gmail.com"
print(nome.count("e"), "\n")


#retorna true ou false para um teste se a string termina com uma string specifica
nome = "felipebtst1@gmail.com"
print(nome.endswith("gmail.com"), "\n")


#encontra a posicção do termo procurado. lembre-se começa do zero
nome = "felipebtst1@gmail.com"
print(nome.find("@"), "\n")


#verifica se o texto é todo feito com letras
nome = "Felipe"
print(nome.isalpha(), "\n")


#verifica se o texto é feito com numeros
nome = "123"
print(nome.isnumeric(), "\n")


#substitui um caractere escolhido por outro
nome = "Felipe"
print(nome.replace("l","I"), "\n")


#separa o texto string baseado em algum caractere indicado
nome = "Felipe @ Nicoli Souza"
print(nome.split("@"), "\n")


#coloca todas as letras iniciais em maiuscula
nome = "felipe bortoluzzi dos santos"
print(nome.title(),"\n")


#retira os caracteres indesejados, como por exemplo espaços que não agragam valor
nome = "  felipe bortoluzzi dos santos  "
print(nome.strip(),"\n")


#retona true ou false para um teste de uma string se inicia com um texto especifico
nome = "felipe 2008"
print(nome.startswith("ser"),"\n")