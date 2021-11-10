d = int(input("Por favor, entre com o número de segundos que deseja converter: "))
a = d / 86400
restoA = d % 86400

b = restoA / 3600
restoB = d % 3600

c = restoB / 60
restoC = d % 60

d = restoC / 1
restoB = d % 1 

print("{:.0f} dias, {:.0f} horas, {:.0f} minutos e {:.0f} segundos.".format(a, b, c, d))
