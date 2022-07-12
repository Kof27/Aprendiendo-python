print("PROGRAMA DE EVALUACIÓN DE NOTAS")

#input hace que el programa se pare hasta que se introduzca un valor 
nota_alumno= input("Introduce la nota del alumno: ")
#de esta forma se va a considerar como texto y no como número
def evaluacion(nota):
	#todos empiezan como aprobado
	valoracion="aprobado"
	#Ahora se inicia el  if para iniciar la comparación 
    #Operadores de comparación: <,>,== (igual que), >=,<=, !=(Diferente que)
	if nota<5:
		valoracion="suspenso"
	return valoracion
#Return --> indica el final de la función pero también el valor que devuelve la función.


print(evaluacion(int(nota_alumno)))
#La forma correcta de hacerlo es ponerle un "int" para transformarlo en un entero