pessoas_presentes=["John Snow","Jesse Pinkman","Aria Stark","Tyrion Lannister"]
chamada = "Aria Stark"
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print("{} está presente".format(chamada))
        break
    else:
        print("Só um print para mostrar que o o sor passou por essa pessoa:"+str(pessoa))

pessoas_presentes=["John Snow","Jesse Pinkman","Aria Stark","Tyrion Lannister"]
chamada = "Aria Stark"
for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print("{} está presente".format(chamada))
        break
    else:
        print("Só um print para mostrar que o o sor passou por essa pessoa:"+str(pessoa))
        continue
    print("Só para mostrar qie ossp não vai ser printado")