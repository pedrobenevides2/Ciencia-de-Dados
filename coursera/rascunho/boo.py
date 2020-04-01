
dec = True
anterior = int(input("Digite o primeiro númeroda sequencia:  "))
valor = 1

while valor!= 0 and dec:
    valor = int(input("Digite o próximo número da sequência:  "))
    if valor > anterior:
        dec = False
    anterior = valor
if dec:
    print( " A sequência está em ordem descrescente!!")
else:
    print( "  A sequeêcnai não está em ordem descrecente!!")
