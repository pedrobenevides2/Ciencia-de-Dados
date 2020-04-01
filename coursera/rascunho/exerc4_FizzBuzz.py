
# Receba um número inteiro na entrada e imprima se o número for divisível por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

a = float(input("Vamos trabalhar.... me diz um número?"))

#print (" O numero inteiro que você escreveu foi", a, " correto?")

b = (a % 5)
e = (a % 3)

c = int(a)

d = ("3 e 5")

if ((b==0) and (e==0)):
    print ( " Esse número é divisível por ",d, "e o valor inteiro dele é ", c)
else:
    print( " Esse número é não é divisível por ",d, "e o valor original é ", a)

