def input_dig():

    x=True
    while x:
        n = input("digite um número: ")
        x = n.isalpha()

    n = int(n)
    print(x)


def input_str():
    x=True
    while x:
        n =input ( "digite uma letra: ")
        x= n.isdigit()

    n= str(n)
    print(x)

