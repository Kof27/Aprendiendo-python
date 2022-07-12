print("EVALUACIÓN DE NOTAS")
#PReferi usar el int directamente en la asignación del valor pues si lo asigno en el print del final va a dar error
nota_alumno= input()

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))