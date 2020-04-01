#soma2

soma=0
valor=1
repet=int(input("Quantos numeros quer somar?  "))
valid=0

while repet!=valid:
    valor = float(input (" Digite um valor a ser somado:  "))
    soma = soma + valor
    valid=valid+1

print( " A soma dos valores digitados é:  ", soma)