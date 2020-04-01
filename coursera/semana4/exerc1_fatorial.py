
def fatorial (x):
    b=1
    c=1

    while x>=b:
        c = c*b
        b=b+1

    return c

n= int(input( "Digite o valor de n:  "))
z=fatorial(n)
print(z)