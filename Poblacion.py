import numpy as np
import random
from Individuo import Individuo
import cv2
class Poblacion:
	def __init__(self,size=300,sizeCircle=1000):
		self.poblacion = []
		self.size = size
		for i in range(self.size):
			ind = Individuo(sizeCircle)
			self.poblacion.append(ind)

	def inicializa(self):
		for i in range(self.size):
			self.poblacion[i].inicializar()
			#self.poblacion[i].decodificar(" "+str(i))
			

	def getIndividuo(self,idx):
		return self.poblacion[idx]

	def setPoblacion(self, poblacion):
		self.poblacion =poblacion.copy()


"""pob = Poblacion()
pob.inicializa()

cv2.waitKey(0)
cv2.destroyAllWindows()	"""

