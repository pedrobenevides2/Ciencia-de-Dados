dig = input("Digite um númeor inteiro:  ")
i = len(dig)
dig= int(dig)
z =1
n1= (dig/(10**(i-1))
n2 = n1%10
n3= int(dig/(10**(i-2)))
n4= n2%10
ajd = False
print (i)

while i!=0 :
    if n2!= n4:
        i = i-1
        n1= int(dig/(10**(i-1)))
        n2 = n1%10
        n3= int(dig/(10**(i-2)))
        n4= n2%10
        print (n1, n4)
    else:
        ajd = True

if ajd:
    print( " Esse numero apresente digitos adjacnte, que são {}, localizados na {} casa decimal ".format(n2, i))
else:
    print( " Esse numero não tem algarismo adjacente")
      
    




