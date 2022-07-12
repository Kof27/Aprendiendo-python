print ("Calificación")

nota = int(input("Por favor introduce tu nota: "))

if nota<5:
	print("Insuficiente ")
elif nota==5:
	print ("Puedes mejorar")
elif nota<6:
	print ("Decente")
elif nota<7:
    print("Sobresaliente")
elif nota ==10:
	print ("Excelente")
else:
	print("Fuera de rango")