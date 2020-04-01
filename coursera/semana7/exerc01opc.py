def primo(x):
    fator = 2
    while x%fator !=0 and fator<=x/2:
        fator=fator+1
    if x%fator==0:
        return False
    else:
        return True

n=int(input('Digite um número acima de 1: '))
w=1

while n>1:
    if primo(n):
        w=w+1
        #print(n)
    n=n-1

print(w)