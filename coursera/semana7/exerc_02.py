


x =int(input('digite a largura:  '))
y= int(input('digite a altura:  '))


x1=x
y1=y
while y>=1:
    while x>0:
        if x==1:
            print("#",end="")
        elif x==x1:
            print("#", end='')
        elif y==1:
            print("#", end='')
        elif y==y1:
            print("#", end='')
        else:
            print(" ",end='')
        x=x-1
    print()
    y=y-1
    x=x1
