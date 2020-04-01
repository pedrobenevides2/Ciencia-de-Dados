
def tabuada():
    x=1
    y=1
    z=1
    while x<=10:
        while y<10:
            z=x*y
            print(f'{x} x {y} = {z}', end ="\t")
            y=y+1
        x=x+1
        print()
        y=1





n=input('Você gostaria da tabuada de 1 a 10?(S/N)  ')
if n== "N":
    print('Ok, bom dia')
else:
    tabuada()