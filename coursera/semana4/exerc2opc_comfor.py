
d = (input("Digite um número: "))

i= len(d)
i1=int(i)
#print(i1)
n1=d[0]
#print (n1)
n2=d[1]
#print (n2)
k=0
w=0
p=1
y=0
for c in range (0,i-1):
    w=int(d[k])
    #print(k)
    print(w)
    y=int(d[p])
    print(y)

    if w!=y:
        r=("não")
    else:
        r=("sim")
    k=k+1
    p=p+1

print(r)