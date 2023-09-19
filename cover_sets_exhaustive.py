from matplotlib_venn import venn2
import matplotlib.pyplot as plt
import numpy as np
from itertools import chain, combinations

class Cover_sets_exhaustive:

	def __init__(self, path, number_of_sets, max_number):

		U = range(1, max_number + 1)
		complete_set = set(range(0,number_of_sets))

		conjunto_potencia = self.powerset(complete_set)
		
		data = []
		file = open(path, 'r')
		
		for linea in file: 
			num = [int(x) for x in  linea.split(',')]
			data.append(num)

		for option in conjunto_potencia:
			numbers_in_option = set()
			option = set(option)

			for set_ in option:
				numbers_in_option.update(data[int(set_)])
			
			if len(numbers_in_option) == len(U):
				print("\n #----------------- Instancia -----------------#")
				print("Solución encontrada")
				print("Seleccione los conjuntos", option)
				break
			

	def powerset(self, iterable):
		s = list(iterable)
		return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


if __name__ == '__main__':

	Cover_sets_exhaustive('Instancia_1.csv', number_of_sets = 8, max_number = 7)
	Cover_sets_exhaustive('Instancia_2.csv', number_of_sets = 10, max_number = 10)
	Cover_sets_exhaustive('Instancia_3.csv', number_of_sets = 9, max_number = 11)