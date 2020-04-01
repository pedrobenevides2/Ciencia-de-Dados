
def soma(x, y):
    return x+y

def multiplica (x, y, z):
    return x*y*z

def matriz (x, y, z, k, v, w):
    return x*k+x*v+x*w+y*k+y*v+y*w+z*k+z*v+z*w

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

def fatorial (x):
    b=1
    c=1

    while x>=b:
        c = c*b
        b=b+1

    
    return c


    

def binomial (x, y):
    
    b = (fatorial(x)/(fatorial(y)*fatorial(x-y)))
    return b

def eq2grau (a, b, c):

    delta = (b**2)-(4*a*c)
    #print(delta)

    if delta<0:
        print( "Solução impossivel pelos números reais, as raizes são complexas")
    
    elif delta ==0:
        x = (-1*b)/(2*a)
    
        print(" A solução apresenta uma única raiz {}".format(x))
    else:
        x1 = ((-1*b)+(((delta)**(1/2))))/(2*a)
        x2 = ((-1*b)-(((delta)**(1/2))))/(2*a)
    
        print("As raizes são reais e valem {} e {}".format(x1, x2))
        

a = int(input(" valor de a "))
b= int(input(" valor de b "))       
c = int(input(" valor de c "))

eq2grau(a, b, c)

    