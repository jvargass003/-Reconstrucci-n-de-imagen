import numpy as np
import random
from Individuo import Individuo

class Seleccion:
	def __init__(self,errores,size=1000):
		self.errores = errores
		self.CopyErrores = errores.copy()
		self.CopyErrores.sort()
		self.size=size
		self.idx = []
		#print(self.errores)
		#print(self.CopyErrores)


	def seleccionar(self):
		mitad = int(self.size/2)
		
		for i in range(self.size):
			if(len(self.idx)==mitad): break
			#print(self.CopyErrores[i])
			if not (self.errores.index(self.CopyErrores[i]) in self.idx):
				#print(self.errores.index(self.CopyErrores[i]))
				self.idx.append(self.errores.index(self.CopyErrores[i]))
		#print(self.idx)
		return self.idx

