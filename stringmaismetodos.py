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