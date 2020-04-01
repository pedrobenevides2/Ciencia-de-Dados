

dig = input("Digite um número inteiro:  ")

i = len(dig)
dig= int(dig)
inc = 0
soma= 0


while inc!=i:

    x= dig %(10)
    dig = dig-x
    dig = dig/10
    soma = soma +x
    inc= inc+1

print( soma)
