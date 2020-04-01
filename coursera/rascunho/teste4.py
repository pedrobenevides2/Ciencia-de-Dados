import math

print ( " vamos calcular sua função? ax2+bx+c")
a= float(input("Qual o valor de a?"))
b= float(input("Qual o valor de b?"))
c= float(input("Qual o valor de c?"))

valorDelta = (b**2)-(4*a*c)
#print(valorDelta) 

if valorDelta>0:
    x1 = (int((-1*b)+(math.sqrt(valorDelta)))/(2*a))
    x2 = (int((-1*b)-(math.sqrt(valorDelta)))/(2*a))
    if x1>x2:
       print(" Seu valores são reias e são {} e {}".format(x2,x1))
    else:
        print(" Seu valores são reias e são {} e {}".format(x1,x2))


 
if valorDelta==0:
        x1=(-1*b)/(2*a)
        print(" Seu valor é unitário, x é igual ", x1)

if valorDelta<0:
        print(" esta equação não possui raízes reais")
