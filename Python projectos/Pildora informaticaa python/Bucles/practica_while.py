#debemos de importar las clases
import math

print("PROGRAMA DE CALCULO RAIZ CUADRADA")
numero=int(input("Introduce el numero por favor: "))

intentos=0

while numero<0:
	print("No se puede hallar la raíz de un numero negativo")

	if intentos==2:
		print("haz consumido demasiados intentos el programa a finalizado")
		#brake; sale del bucle
		break;
	numero=int(input("Introduce el numero por favor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	#math es una clase
	solucion=math.sqrt(numero)
	print("la raiz cuadrada de " + str(numero) + " es " + str(solucion))