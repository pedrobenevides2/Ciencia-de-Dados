

def  usuario_escolhe_jogada(n, m):
    r1 = 1
    r1 = int((input ( "Quantas peças? ")))
    while not (r1>0 and r1<(m+1) and r1<n):
        r1 = int(input( " o numero tem que ser maior que 0 e menor do que {} e não pode ser maior que {} ".format(m+1, n)))

def computador_escolhe_jogada(n,m):

    w = int(n/(m+1))
    rpc=1

    if w==0:
        w=1
    else:
        w=w

    rpc = int((n- (w*(m+1)))
    
def partida():
    
    n = int(input("Quantas peças?  "))
    m = int(input("Limite de peças por jogada?  "))

    z = m+1
    k=0

    if n%z==0:
        p1= print(" Você começa ")
        k=1

    else:
        pc=print( "Eu começo ")
        k=0

    r1=1
    rpc=1

    if k==1:
        while not n==0:
           
            usuario_escolhe_jogada(n,m)
            n = n -r1
            computador_escolhe_jogada(n,m)
            print( " O computador retira {} peças". format(rpc))
            n=n-rpc
            print ( " sobraram {} peças".format(n))
        print (" Fim do jogo! O computador ganhou! ")
    elif k==0:
        while not n==0:
            computador_escolhe_jogada(n,m)
            print( " O pc retira {} peças". format(rpc))
            n=n-rpc
            usuario_escolhe_jogada(n,m)
            n = n -r1
            print ( " sobraram {} peças".format(n))
        print( " Fim do jogo! O computador ganhou!")
    


# jogo

partida()
