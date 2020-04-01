import random

n = int(random.randrange(0,5))
z = int(input(" Qual foi o numero que o PC escolheu?"))

if n==z:
    print(" parabens, você acertou. Confirmando o número, ele foi {}".format (n))
else:
    print ( " Vc errou o numero, o numero escolhido pel o Pc foi {}". format (n))
