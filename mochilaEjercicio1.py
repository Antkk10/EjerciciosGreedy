#!/usr/bin/python

"""Funcion que selecciona el mejor objeto en funcion de su relacion
beneficio/peso. La variable solucion contiene 1 si el objeto que ocupa
la posicion i ha sido seleccionado y 0 si no ha sido seleccionado.
Devuelve la posicion que ocupa el objeto en los vectores beneficio y peso. """
def Seleccionar(beneficio, peso, solucion):
	
	indiceAct = -1 # Actualmente no tenemos indice seleccionado
	comparacion = 0 # Lo usamos para almacenar el b/p del indice actual
	cantidad = len(beneficio) # obtenemos la cantidad de numeros del vector
	# iteramos sobre los dos vectores
	for i in range(0, cantidad):
		# No tenemos indice y el objeto no ha sido seleccionado.
		if indiceAct == -1 and solucion[i] == 0:
			indiceAct = i # indice del objeto mas prometedor hasta ese momento.
			comparacion = beneficio[i] / peso[i]
		# el objeto[i] es mejor que el actual y no ha sido guardado en la mochila.
		elif beneficio[i] / peso[i] > comparacion and solucion[i] == 0:
			comparacion = beneficio[i] / peso[i]
			indiceAct = i

	return indiceAct # Devolvemos el indice del objeto mas prometedor

"""Decimos que el ejercicio tiene solucion cuando en el vector sol almenos
hay un objeto seleccionado. """
def Solucion(sol):
	
	for i in (0, len(sol)):
		if(sol[i] == 1): # Al menos un objeto seleccionado.
			return True 

	return False # no hay ningun objeto seleccionado.

"""Funcion en el cual usamos un algoritmo Greedy de seleccion de objetos
y que "guardamos" en la mochila.
Variable b es un vector que indica el beneficio del objeto de la posicion iesima
Variable p es un vector que indica el peso del objeto de la posicion iesima.
Variable s es un vector en el cual si la posicion iesima tiene un 0, el objeto
no ha sido seleccionado, 1 indica que el objeto si ha sido seleccionado.
Variable M indica el peso maximo que soporta la mochila. """
def Mochila(b, p, s, M):

	pesoAct = 0 # indica el peso actual en la mochila.

	for i in range(0, len(b)): # itera sobre todos los objetos de la mochila
		s.append(0)
		


	while pesoAct < M:
		x = Seleccionar(b, p, s) # Seleccionamos el mejor obj disponible

		if (p[x] + pesoAct) <= M:
			s[x] = 1 # Seleccionamos el obj
			pesoAct += p[x] # Actualizamos el peso total hasta este momento
		else:
			s[x] = (M - pesoAct) * 1.0 / p[x] # Fraccionamos el obj
			pesoAct = M # Actualizamos el peso total hasta este momento

	

	# Si hay obj seleccionado
	if Solucion(s):
		return True

	return False

if __name__ == "__main__":

	M = 15 # Peso de la mochila
	# Beneficio del obj posicion iesima
	beneficio = [10, 5, 15, 7, 6, 18, 3]
	# Peso del obj posicion iesima
	peso = [2, 3, 5, 7, 1, 4, 1]
	# Vector solucion de los obj seleccionados
	solucion = []

	if Mochila(beneficio, peso, solucion, M):
		print "Existe solucion. "
		print "Los objetos seleccionados son los siguientes: "

		for i in range(0, len(solucion)):
			if solucion[i] == 1:
				print "Objeto numero: ", i, " seleccionado."
			elif solucion[i] != 0:
				print "objeto numero: ", i, " cogemos parte ", solucion[i]

	else:
		print "No existe solucion."
