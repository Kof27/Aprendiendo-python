#Transformar Tupla en lista
mitupla=("Juan",15,5949)
lista = list(mitupla)
print (lista[:])


#transmormar lista en tupla
lista1=["Juan",15,15,5949]
mitupla1=tuple (lista1)
print (mitupla1)
#Contar cuantas veces se repite un elemento en una dupla .count
print(mitupla1.count(15))
#.len es para calcular cuantos elementos hay
print(len(mitupla1))
#para almacenar información en una variable (desempaquetado de tuplas)
lista1=["Juan",15,15,5949]
mitupla1=tuple (lista1)
print (mitupla1)
nombre,dia,mes,agno =mitupla1
print (nombre, dia, mes, agno)
