
# Receba um número inteiro na entrada e imprima se o número for divisível por 3.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

a = float(input("Vamos trabalhar.... me diz um número?"))

print (" O numero inteiro que você escreveu foi", a, " correto?")

b = (a % 3)

c = int(a)

if (b==0):
    print ( " Esse número é divisível por 3 e o valor inteiro dele é ", c)
else:
    print( " Esse número é não é divisível por 3 e o valor original é ", a)

print( "Bjo e me liga")