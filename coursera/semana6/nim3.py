

def  usuario_escolhe_jogada(n,m):#ok
    
    r1 = int((input ( "Quantas peças você vai retirar? ")))
   
 
    if r1<1:
        while r1<1:
                r1= int(input(" O número tem que ser maior que zero "))
    elif r1>m:
        while r1>m:
                r1= int(input(" o número tem tem que ser igual ou menor que {}  ".format(m)))
    elif r1>n:
        while r1>n:
                r1+ int(input(" O número não pode ser maio que tem na mesa"))
   
    z = n-r1
   
    print(" Você tirou {} peças".format(r1))
    print( " Restam {} peças no jogo".format(z))
    return z


def computador_escolhe_jogada(n,m):#ok

    rpc =1
    z = m+1
    w= n/z
    w = int(w)
    if w==0:
        w=1
    else:
        w=w
    rpc = n-(w*z)
    n=n-rpc

    print("O computador retirou {} peças".format(rpc))
    print ( " Restam {} pecas no jogo".format(n))
    return n

def jogo():
    n = int(input("Quantas peças ?  "))
    m = int(input("Limite de peças por jogada?  "))
   
    k=0

    if n%(m+1)==0:
        p1= print(" Você começa ")
        k=1

    else:
        pc=print( "Eu começo ")
        k=0


    #ok


    if k==1:
        while not n<1:

           n = usuario_escolhe_jogada(n,m)
           n = computador_escolhe_jogada(n,m)
     
           
        
    if k==0:
        while not n<1:
            computador_escolhe_jogada(n,m)
            n=n-rpc
            print (" o computador retirou {} pecas".format(rpc))
            print( " Restam {} peças no jogo".format(n))
            usuario_escolhe_jogada(n,m)
            n=n-r1
            print ( " Restam {} pecas no jogo".format(n))
    print( " computador ganhou")
    
    
      





jogo()
