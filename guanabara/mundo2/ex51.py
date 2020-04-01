print(" TERMOS DE UMA PA")

p = int(input(" Primeiro termo:  ")) #primeiro termo
r =int ( input(" Razão:  "))         # razão
d = p + (10-1)*r                    # décimo termo

for c in range (p,d, r):
    print("{}".format(c), end=" -> ",)
print ("Acabou")

