
n=input("Digeite um número: ")
i =int(len(n))
#print(i)
n=int(n)

while i!=1:
    #print(n)
    n1=n//(10**(i-1))
    #print(n1)
    n2=(n%(10**(i-1)))//(10**(i-2))
    #print(n2)
    n=(n%(10**(i-1)))
    #print(n)
    i=i-1
    #print(i)
    if i==0:
        break