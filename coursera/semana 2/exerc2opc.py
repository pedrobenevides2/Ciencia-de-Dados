a = int(input("Por favor, entre com o número de segundos que deseja converter: "))

z = 60*60*24 # dia
k = 60*60 #hora
w = 60 # minuto
x = 0 # segundos

ad=a//z
#print (ad)
adr = a%z
#print(adr)
ah = adr //k
#print(ah)
adr = adr%k
#print(adr)
am = adr//w
#print (am)
ass = adr%w 
#print(ass)

print("{} dias, {} horas, {} minutos e {} segundos".format(ad, ah, am, ass))