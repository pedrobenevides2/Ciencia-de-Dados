n = int(input(" Me diga um numnero?"))
b = int(input(" Em quak base você quer: binário (1); Octal (2); Hexadecimal(3)"))


if b==1:
    z= n%2
    print(z)
elif b==2:
    z= n%8
    print(z)
elif b==3:
    z=n%9
    print(z)

else:
    print(" vc não escolheu uma base valida")
    