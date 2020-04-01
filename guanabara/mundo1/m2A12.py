

nome = str(input("Qaul é o sei nome? "))

if nome=="Gustavo":
    print(" Que nome de bundão")
elif nome=="Pedro" or nome=="Maria" or nome=="Ana":
    print(" Gostei desse nome em....")
elif nome in "tiago claudia":
    print(" Ok...podemos trabalhar com isso")
else:
    print("podemos melhor esse nome em... ")

print("Tenha um bom dia {}".format(nome))

