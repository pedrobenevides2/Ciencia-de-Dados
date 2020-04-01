x = int(input("Digite um número: "))
b = 0
c = 0
for c in range (1,x+1):
    
    if x%c ==0:
        b = b+1
        print('{} '.format(c))
        
        
print ('\n Número  {} foi divisível {} vezes.'. format(x, b))    

        
if b == 2:
    print( " \n É um numero primo", end= " ")


 
