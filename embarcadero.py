
"""
Enunciado:
	Sobre un rio navegable hay n embarcaderos. En cada uno de ellos se puede
	alquilar un bote que permite ir a cualquier otro embarcadero rio abajo(ya
	que es imposible ir rio arriba). Existe una tabla de tarifas T[i, j]
	que indica el coste del viaje del embarcadero i al j para cualquier embarcadero
	de partida i y cualquier embarcadero de llegada j mas abajo del rio (i < j)

	Puede suceder que un viaje de i a j sea más caro que una sucesión de viajes
	más cortos, en cuyo caso se tomaria un primer bote hasta un embarcadero k 
	y un segundo bote para continuar a partir de k. No hay coste adicional
	por cambiar de bote.

Respuesta:
	Este ejercicio se ajusta perfectamente a utilizar el algoritmo de Dijkstra
	para obtener el camino más corto de un nodo a otro. Además tenemos un grafo
	dirigido ya que se puede navegar por ejemplo de un nodo 2 a un nodo 3
	pero no viceversa. 	
"""

from queue import PriorityQueue
import math # Para usar infinito
"""
	Función que usamos para aplicar el algoritmo de Dijkstra.
	parámetro embarcaderos: es una matriz con los caminos i,j teniendo
	valores i < j.
	parámetro camino: es un map que indica el camino que lleva desde un sitio
	a otro.
	parámetro inicio: entero que indica el nodo inicio.
"""
def Dijkstra(embarcaderos, camino, inicio):
	# Almacenamos el coste mínimo para cada nodo.
	coste = []

	# Iniciamos el coste y el camino de cada nodo
	for i in range(0, len(embarcaderos)):
		coste.append(math.inf)
		camino.append(-1)

	# El inicio empieza en el nodo inicio
	camino[inicio] = inicio
	# El coste inicial es 0
	coste[inicio] = 0

	# Declaramos la cola con prioridad
	cola = PriorityQueue(0)

	# Metemos en la cola todos los caminos desde el nodo inicio
	for i in range(inicio+1, len(embarcaderos[inicio])):
		# Insertamos el coste, el nodo destino y nodo origen
		cola.put((embarcaderos[inicio][i], i, inicio))

	# Mientras que la cola no esté vacia
	while not cola.empty():
		datos= cola.get() # Obtenemos el mejor camino
		dest = datos[1] # nodo destino
		org = datos[2] # nodo origen

		if coste[dest] > (coste[org] + embarcaderos[org][dest]):
			coste[dest] = coste[org] + embarcaderos[org][dest]
			camino[dest] = org
		


if __name__ == "__main__":

	camino = []
	embarcaderos = []

	embarcaderos.append([])
	embarcaderos[0].append(0)
	embarcaderos[0].append(5)
	embarcaderos[0].append(3)
	embarcaderos[0].append(9)
	embarcaderos[0].append(14)


	embarcaderos.append([])

	embarcaderos[1].append(0)
	embarcaderos[1].append(0)
	embarcaderos[1].append(3)
	embarcaderos[1].append(2)
	embarcaderos[1].append(3)


	embarcaderos.append([])

	embarcaderos[2].append(0)
	embarcaderos[2].append(0)
	embarcaderos[2].append(0)
	embarcaderos[2].append(4)
	embarcaderos[2].append(4)


	embarcaderos.append([])

	embarcaderos[3].append(0)
	embarcaderos[3].append(0)
	embarcaderos[3].append(0)
	embarcaderos[3].append(0)
	embarcaderos[3].append(2)


	embarcaderos.append([])

	embarcaderos[4].append(0)
	embarcaderos[4].append(0)
	embarcaderos[4].append(0)
	embarcaderos[4].append(0)
	embarcaderos[4].append(0)

	Dijkstra(embarcaderos, camino, 0)