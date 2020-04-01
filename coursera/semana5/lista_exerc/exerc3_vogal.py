

def vogal(k):

    n=k.lower()
    #print(n)
    vogal =('a','e','i','o','u')
    #print(vogal[0:5])
    b=0
    for letra in vogal:
        if letra == n:
            b=b+1
        else:
            b=b
    if b==0:
        b = False
    else:
        b =True
    return b


# Execução
x = input("vogal ")


while x.isdigit():
    x = input( "vogal ")

p=True
p= vogal(x)