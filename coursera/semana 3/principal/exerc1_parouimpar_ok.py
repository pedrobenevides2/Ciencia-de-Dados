def impar (x):
    if x%2==0:
        return False
    else:
        return True


n  = int(input(" Digite um número inteiro: "))

if impar(n):
    print(" ímpar")
else:
    print("par")
