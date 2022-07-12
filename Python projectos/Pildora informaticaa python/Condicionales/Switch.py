print("PROGRAMA DE BECAS 2022")
distancia_escuela=int(input("Introduce la distancia a la escuela en KM: "  ))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos que posees: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario total que gana tu familia anualemente en bruto: "))
print(salario_familiar)

#Operadores logicos= Si se usa siempre "and" se obliga a cumplir las condiciones, mientras que el "or" se puede traducir como y si no
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=50000:
	print("Tienes derecho a beca")
	print("felicidades")
else:
	print("No tienes derecho a beca")
