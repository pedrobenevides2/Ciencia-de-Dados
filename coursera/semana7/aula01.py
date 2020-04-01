
def fatorial(x):
    d = 1
    z=1
    while d<=x-1:
        d=d+1
        z=z*d


    return z


n = int(input(" digite um número inteiro possitivo:  "))
while n<=0:
    n = int(input(" digite um número inteiro possitivo:  "))
n= fatorial(n)
print (n)
