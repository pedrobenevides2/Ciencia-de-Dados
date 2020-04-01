
n = int(input("Digite o valor de n: "))
d = 1 #fator
b = 1 #x

def primo(x):
    fator = 2
    while x%fator !=0 and fator<=x/2:
        fator=fator+1
    if x%fator==0:
        return False
    else:
        return True

def impar (x):
    if x%2==0:
        return False
    else:
        return True

while b<=n:
    if primo(b) and impar(b):
        print (b)
    b=b+1

  