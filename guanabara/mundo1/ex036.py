
valorCasa = int( input(" Qual é o valro da casa? "))

salariao = int(input('Qual é o seu salário? '))

tempoAno = int(input(" Em quantos anos você pretende pagar? "))

tempMes = tempoAno * 12

prestacao = float(valorCasa/tempMes)


if (prestacao/salariao)<( 0.3*salariao):
    print(" A prestação da sua casa será de {:.2f}".format(prestacao))
else:
    print ("Seu salário não é o sufuciente para pagar a prestação de {:.2f}".format(prestacao))