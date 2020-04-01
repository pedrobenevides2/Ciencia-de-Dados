
def maximo (a, b):
    if a>b:
        c = a
        return c
    elif a<b:
        c = b
        return c
    else:
        c  =  a
        return c

def teste_maximo():
    assert maximo( 5, 4) ==5
    assert maximo(4, 5)==5
    assert maximo (5, 5)==("Ambos os número são iguais")

x = int(input("primeiro numero"))
y= int( input("Segundo numero"))

print(maximo(x,y))
