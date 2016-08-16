#!/usr/bin/python

from Queue import PriorityQueue

"""
	El ejercicio consiste en establecer una red de distribucion de periodicos
	desde la ciudad A a otras 10 ciudades. La distribucion se va ramificando a traves
	de las ciudades. Los kms. de distancia entre ciudades viene representada
	en un map con dos casillas. La primera casilla representa la distancia en kms
	y la segunda casilla representa a la ciudad. La llava del map es la ciudad
	que almacena dicho vector.

	Para resolver el ejercicio he implementado el algoritmo de Prim que consiste
	en seleccionar de un conjunto de vertices no seleccionados la arista de menor
	coste que conecta con uno de los vertices seleccionados.
"""

"""
	Funcion que crea el camino a cada nodo usando el algoritmo de Prim. Recibe dos parametros,
	caminos que es un map y que cada clave contiene un vector con dos campos, el primero
	los kms desde el nodo origen (llave) hasta el nodo destino que es representado en el segundo
	campo. El parametro padre es un map que la llave representa el nodo destino y esta asociada
	a un valor que representa el nodo origen. 
	Lo que se pretende con esta funcion es asignar los nodos origen en el map padre para poder
	obtener un camino ramificado.
"""
def Prim(caminos, padre):

	#Obtenemos el nodo ratiz que es el mismo en el map padre
	raiz = 0

	for i in padre:
		if i == padre[i]:
			raiz = i
			break

	# Iniciamos una cola con prioridad con los nodos hijos del nodo raiz
	cola = PriorityQueue(0)
	for j in caminos[raiz]:
		# Primer campo es el coste de ir desde tercer campo (nodo padre) hasta
		# el segundo campo (nodo destino o hijo)
		cola.put((j[0],j[1], raiz))
		


	# Construimos el camino para cada nodo
	while not cola.empty():
		# Obtenemos la distancia, destino y origen de la distancia mas corta.
		dist, dest, org = cola.get()
		# Si todavia no hemos ido a la ciudad destino
		if padre[dest] == 0:
			# Actualizamos el padre del destino
			padre[dest] = org
			# Insertamos todos los hijos del destino en la cola
			for i in caminos[dest]:
				cola.put((i[0], i[1], dest))
				


"""
	Funcion que se utiliza para mostrar el camino que va desde el nodo origen
	hasta un nodo concreto.
	El parametro padre representa un map con los caminos a cada nodo.
"""
def MostrarRuta(padre):
	# Obtenemos el nodo raiz,
	raiz = 0

	for i in padre:
		if padre[i] == i:
			raiz =i
			break
	
	for i in padre:
		# pila es una lista que usamos como heap
		pila = [] 
		fin = False
		# j son los nodos que iremos metiendo en la pila
		j = i
		while True:
			pila.append(j)
			# Hemos llegado al nodo origen, salimos de while
			if j == raiz:
				break
			else:
				j = padre[j]

		
		numElementos = len(pila) # Numero de elementos de la pila
		# Mostramos el camino del nodo origen hasta el nodo i
		print "El camino hacia ", i, " es el siguiente: "
		for i in range(0, numElementos):
			print pila.pop()
	print "La raiz ", raiz

if __name__ == "__main__":

	# Iniciamos el padre de cada nodo a 0 excepto nodo a que es donde empezamos
	padre = {'a' : 'a'}

	
	for i in map(chr, range(98, 108)):
		padre[i] = 0

	
	# Iniciamos los caminos de cada nodo. Lo ideal seria que lo tuvieramos
	# en un archivo de texto.
	# Tenemos una matriz con 11 filas y 2 columnas
	# primera columna representa los kms, y la segunda casilla la ciudad.
	caminos = {'a' : [(40, 'b'), (45, 'c'), (50, 'd'), (45, 'e'), (30, 'f'), (60, 'k')]}
	caminos['b'] = [(25, 'g'), (60, 'h'), (50, 'j'), (40, 'a')]
	caminos['c'] = [(45, 'a'), (25, 'i')]
	caminos['d'] = [(50, 'a'), (25, 'i'), (45, 'k')]
	caminos['e'] = [(45, 'a'),(40, 'f'), (10, 'k')]
	caminos['f'] = [(30, 'a'), (40, 'e'), (40, 'g')]
	caminos['g'] = [(25, 'b'),(40, 'f'), (20, 'j')]
	caminos['h'] = [(60, 'b'), (10, 'i'), (10, 'j')]
	caminos['i'] = [(25, 'c'), (25, 'd'), (10, 'h')]
	caminos['j'] = [(50, 'b'), (20, 'g'), (10, 'h')]
	caminos['k'] = [(60, 'a'), (45, 'd'), (10, 'e')]


	Prim(caminos, padre)
	MostrarRuta(padre)

	
