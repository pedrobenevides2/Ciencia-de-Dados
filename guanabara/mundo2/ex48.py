b = 0
cont = 0
for c in range (1,501, 2):
    if c%3==0:
        b = b+c
        cont = cont+1
        #print(c)

print("Soma dos valores são {}, com a soma de {} números".format(b,c))

