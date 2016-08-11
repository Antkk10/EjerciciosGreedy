#!/usr/bin/python

""" Enunciado:
	Seleccione un lote de 100 libros, lo mas barato posible, de entre
	los siguientes lotes:
		25 volumenes 65.000 Ptas/Lote
		10 volumenes 30.000 Ptas/Lote
		100 volumenes 270.000 Ptas/Lote
		80 volumenes 16.000 Ptas/Lote
"""

"""
	Funcion de seleccion del lote de libros mas barato de los que quedan
	por selecconar. Para la seleccion de lotes, dividimos el lote por el precio
	para obtener el precio del libro dentro de ese lote. Con esta operacion
	obtenemos el lote de libros mas barato.
"""
def Seleccionar(lote, precio, solucion):
	
	indiceAct = -1 # Actualmente no tenemos indice seleccionado
	comparacion = 0 # Lo usamos para almacenar el precio/lote del indice actual
	cantidad = len(lote) # obtenemos la cantidad de indices del vector
	# iteramos sobre los dos vectores
	for i in range(0, cantidad):
		# No tenemos indice y el objeto no ha sido seleccionado.
		if indiceAct == -1 and solucion[i] == 0:
			indiceAct = i # indice del objeto mas prometedor hasta ese momento.
			comparacion = precio[i] / lote[i]
		# el objeto[i] es mejor que el actual y no ha sido guardado en la mochila.
		elif precio[i] / lote[i] < comparacion and solucion[i] == 0:
			comparacion = precio[i] / lote[i]
			indiceAct = i

	return indiceAct # Devolvemos el indice del objeto mas prometedor

"""Decimos que el ejercicio tiene solucion cuando en el vector sol almenos
hay un objeto seleccionado. """
def Solucion(sol):
	
	for i in (0, len(sol)):
		if(sol[i] != 1): # Al menos un objeto seleccionado.
			return True 

	return False # no hay ningun objeto seleccionado.

"""Funcion en el cual usamos un algoritmo Greedy de seleccion de objetos
y que "guardamos" en la mochila.
Variable l es un vector que indica el lote de libros de la posicion iesima
Variable p es un vector que indica el precio del lote de la posicion iesima.
Variable s es un vector en el cual si la posicion iesima tiene un 0, el objeto
no ha sido seleccionado, 1 indica que el objeto si ha sido seleccionado.
Variable M indica el tope maximo de libros """
def Mochila(l, p, s, M):

	librosAct = 0 # indica el numero de libros actual en la mochila

	for i in range(0, len(l)): # inicializamos el vector solucion
		s.append(0)
		


	while librosAct < M:
		x = Seleccionar(l, p, s) # Seleccionamos el lote mas barato disponible

		if (l[x] + librosAct) <= M:
			s[x] = 1 # Seleccionamos el obj
			librosAct += l[x] # Actualizamos la cantidad de libros actual
		else:
			s[x] = (M - librosAct) * 1.0 / l[x] # Fraccionamos el lote
			librosAct = M # Actualizamos los libros actuales hasta ese momento

	

	# Si hay obj seleccionado
	if Solucion(s):
		return True

	return False

if __name__ == "__main__":

	M = 100  # tope de libros
	# Lote de libros
	libros = [25, 10, 100, 80]
	# Precio de cada lote
	precio = [65000, 30000, 270000, 160000]
	# Vector solucion de lotes seleccionados
	solucion = []

	precioTotal = 0 # Precio total a pagar
	if Mochila(libros, precio, solucion, M):
		print "Existe solucion. "
		print "Los lotes seleccionados son los siguientes: "

		for i in range(0, len(solucion)):
			if solucion[i] == 1:
				print "Lote numero ", i, " seleccionado:", libros[i]
				precioTotal += precio[i] 
			elif solucion[i] != 0:
				print "Lote numero ", i, " seleccionamos: ", int(solucion[i] * libros[i])
				precioTotal += (libros[i] / precio[i]) * int(solucion[i] * libros[i])

		print "El precio total es: ", precioTotal
	else:
		print "No existe solucion."
