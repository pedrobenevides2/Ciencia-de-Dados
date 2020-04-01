def primo(x):
    fator = 2
    while x%fator !=0 and fator<=x/2:
        fator=fator+1
    if x%fator==0:
        return False
    else:
        return True


n = int(input(" Digite um número inteiro maior que 1:  "))

fator = 2
multiplicidade=0

while n>1:
    while n % fator ==0:
        multiplicidade = multiplicidade+1
        n=n/fator
        if primo(fator):
            print("{} é um numero primo".format(fator))
    if multiplicidade>0:
        print("fator {} multoplicidade = {} ".format(fator, multiplicidade))
    fator=fator+1

    multiplicidade=0

