def primo(k):
    fator = 2
    while k%fator !=0 and fator<=k/2:
        fator=fator+1
    if k%fator==0:
        return False
    else:
        return True


def maior_primo(k):

    while k<2:
        k = int(input( " Digite número inteiro maior ou igual a 2: "))

    d= éPrimo(k)
    return d

def éPrimo(z):

    b = primo(z)

    while not b:
        z=z-1
        b = primo(z)
    print (z)
    return z


w = int(input("Digite um número: "))
s=0
s= maior_primo(w)
