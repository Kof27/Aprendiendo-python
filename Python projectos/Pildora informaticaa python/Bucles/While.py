edad=int(input("Por favor introduce tu edad: "))

while edad<0 or edad>=100:
	print("Edad fuera de rango")
	edad=int(input("Introduce nuevamente tu edad: "))

print("Gracias por colaborar")
print("Tu edad es " + str(edad))