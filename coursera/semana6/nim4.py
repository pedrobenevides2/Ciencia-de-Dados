

def  usuario_escolhe_jogada(n,m):#ok1

    q=0

    while q==0:
     r1 = int((input ( "Quantas peças você vai tirar? ")))
     if ((r1>0) and (r1<(n+1)) and (r1< (m+1))):
         break
     else:
         print("\n Oops! Jogada inválida! Tente de novo.\n")

    z = n-r1

    print(" Você tirou {} peças".format(r1))

    if z==1:
        print('Agora resta apenas uma peça no tabuleiro.')
    else:
        print( "Agora restam {} peças no tabuleiro.".format(z))
    return z


def computador_escolhe_jogada(n,m):#ok

    rpc =1
    z = m+1
    w= n/z
    print(w)
    w = round(w-0.5)
    print(w)
    if w==0:
        w=1
    else:
        w=w

    if n>m:
        rpc = n-(w*z)
    elif n<=m:
        rpc = n

    n=n-rpc

    if rpc==1:
        print('\nO computador tirou uma peça.')
    else:
        print("O computador retirou {} peças".format(rpc))
    if n!=0:
        print ( "Agora restam {} pecas no tabuleiro\n".format(n))
    return n

def partida():
    n = int(input("Quantas peças ?  "))
    m = int(input("Limite de peças por jogada?  "))
    print("")

    k=0

    if n%m==1:
        p1= print("\n Você começa!")
        k=1

    else:
        pc=print( "\nComputador começa!")
        k=0



    if k==1:
        while not n==0:

           n = usuario_escolhe_jogada(n,m)
           n = computador_escolhe_jogada(n,m)

    if k==0:
        while not n==0:
            n= computador_escolhe_jogada(n,m)
            if n==0:
                break
            n =usuario_escolhe_jogada(n,m)



    print( "Fim do jogo! O computador ganhou!")

def campeonato():
    print ('Bem-vindo ao jogo NUM! Escolha:\n')
    print (" 1 - para jogar uma partida isolada ")
    print (" 2- para jogar um campeonato \n ")
    cp = int(input(""))

    if cp ==1:
        print( " Você escolheu uma partida solo\n")
    elif cp ==2:
        print("Você escolheu um campeonato !\n")
    else:
        print ( " Você fez uma escolha inválida. Fim do jogo\n")


    if cp==1:
        print (" **** Rodada Única ****\n")
        partida()

    elif cp==2:
        print ("\n**** Rodada 1****\n")
        partida()
        print ("\n**** Rodada 2 ****\n")
        partida()
        print ("\n**** Rodada 3 ****\n")
        partida()
        print("\n**** Final do campeonato****")
        print("\n Placar: Você 0 x 3 Computador")







campeonato()