from matplotlib_venn import venn2
import matplotlib.pyplot as plt
import numpy as np
import heapq 

class Cover_Sets:

	def __init__(self, path, max_number):
		
		datos = open(path)

		self.Dic = {}
		self.Solucion  = []
		Conjuntos = []
		numeros_agregados = set()
		Conjunto_Mejor = 0

		for number, row in enumerate(datos):
			row = row.replace("\n", "")
			lista = row.split(',')
			numeros = [int(numero) for numero in lista]
			
			self.Dic[number] = numeros
			if len(numeros) > Conjunto_Mejor:
				Mejor_opcion = (len(numeros), set(numeros), number)
				Conjunto_Mejor = len(numeros)

			else:
				Conjuntos.append((len(numeros), set(numeros), number))

		self.Solucion.append(Mejor_opcion[2])
		numeros_agregados.update(Mejor_opcion[1])
		

		while len(numeros_agregados) < max_number:
			Restantes = [ max_number - len( numeros_agregados | Conjuntos[i][1] ) for i in range(len(Conjuntos))]
			Indice = np.argmin(Restantes)
			
			numeros_agregados = numeros_agregados | Conjuntos[Indice][1]
			self.Solucion.append(Conjuntos[Indice][2])
		
		print("\n #----------------- Instancia -----------------#")
		print("Conjuntos")
		for i,j in self.Dic.items():
			print("Conjunto", i,  "| Items ", j )
		
		print("\nSolución: Seleccionar los conjuntos", self.Solucion)

	
if __name__ == '__main__':

	Cover_Sets('Instancia_1.csv', 7)
	Cover_Sets('Instancia_2.csv', 10)
	Cover_Sets('Instancia_3.csv', 11)
	