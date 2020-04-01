def maximo (a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>b and c>a:
        return c
    else:
        return a


x = int(input("primeiro numero"))
y= int( input("Segundo numero"))
z = int( input("terceiro numero"))


w=maximo(x,y,z)

print(w)