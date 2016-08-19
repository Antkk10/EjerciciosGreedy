
#!/usr/bin/python

from Queue import PriorityQueue

"""
Enunciado:
	Un vertice p de un grafo dirigido G = (V,A) se dice es un pozo o sumidero
	si hay arcos en el grafo que lo tienen como extremo y ninguno como origen. 
	Desarrolle un algoritmo que detecte la presencia de pozos en un grafo G.

Respuesta:

	Un nodo es pozo cuando en el grafo dirigido un nodo "padre" puede viajar
	hacia ese nodo, pero de ese nodo "pozo" no se puede viajar hacia otro nodo
	ya que de el no sale ninguna arista hacia otro nodo.

	Vamos a usar el algoritmo de Prim para construir el arbol de caminos aunque
	realmente no se utilice con grafos dirigidos.

"""

"""
	Algoritmo de Prim en el que recibe un conjuto de nodos y crea
	los caminos entre nodos. Para construir el camino, recibe un nodo
	raiz, sus adyacentes los metemos en una cola con prioridad. Posteriormente
	sacamos el arco con la distancia mas corta entre nodos dentro de la cola.
	Si ese nodo no tiene asignado un padre, se lo asignamos, dicho padres es
	el nodo origen que lleva hacia el nodo sacado de la cola por la distancia
	mas corta. Una vez asignado el nodo padre, introducimos sus adyacentes en la 
	cola para continuar construyendo el arbol.

	El parametro nodos es un map que contiene un vector. Cada posicion del
	vector se corresponde con una pareja de valores, el primer valor es 
	la distancia del nodo llave hacia la segundo valor que es el nodo destino.
	El parametro padres contiene un nodo origen que lleva hacia el nodo destino
	representado por la llave del parametro padre. Este parametro es un map.
	raiz es el nodo donde comienza a construirse el arbol por el algoritmo de Prim.
"""
def Prim(nodos, padres, raiz):
	# Construimos la cola con limite indefinido
	cola = PriorityQueue(0)

	# Insertamos los nodos adyacentes del nodo raiz en la cola
	for i in nodos[raiz]:
		cola.put((i[0], i[1], raiz))
	# Mientras que la cola no sea vacia.
	while( not cola.empty()):
		# Obtenemos la distancia, destino y origen
		dist, dest, org = cola.get()

		# Si todavia no hemos ido a la ciudad destino
		if(padres[dest] == 0):
			padres[dest] = org

			# Insertamos en la cola los adyacentes de predecesores
			for i in nodos[dest]:
				cola.put((i[0], i[1], dest))

"""
	Funcion que nos dice si un nodo es pozo o no.
	padres es un map que cada llave del map esta asociado a un nodo padre.
	nodo contiene el valor para comprobar si es pozo.
"""
def Pozo(predecesores, nodo):

	# Comprobamos si por cada nodo, su padre es el nodo buscado.
	for n in predecesores:
		# El nodo buscado no es pozo
		if predecesores[n] == nodo:
			return False

	return True


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


	Prim(caminos, padre, 'a')

	for n in padre:
		if Pozo(padre, n):
			print ("El nodo ", n, " es nodo Pozo.")
		else:
			print ("El nodo ", n, " NO es nodo Pozo.")
