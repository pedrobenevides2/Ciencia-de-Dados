# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente,
#  às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder,respectivamente, 
# às coordenadas x e y de um outro ponto no mesmo plano.Calcule a distância entre os dois pontos. Se a distância 
# for maior ou igual a 10, imprima longe na saída. Caso o contrário, quando a distância for menor que 10, imprima perto

print (" Já está cansado...eu tambem....\n Então vamos ver quanto nossa preguiça vai achar dessa caminhada")

print( " Preciso que você me de as coordenadas X e Y do local de saída e do local de chegada")

x1 = float(input(" X do local de saida "))
y1 = float(input(" Y do local de saída "))
x2 = float( input("X do local de chegada "))
y2 = float( input("Y do local de chegada "))

d = (((x1-x2)**2)+(y1-y2)**2)**(0.5)

if(d >= 10):
    print("Preguiça ...deu ruim... é longe")
else:
    print( "ai preguiça.. nem foi tão ruim.... é perto")