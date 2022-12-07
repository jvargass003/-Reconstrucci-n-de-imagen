import numpy as np
import random
from Individuo import Individuo
import cv2

class Funcion():
	def __init__(self,imagen,individuo,sizeImage=300):
		individuo.decodificar()
		self.individuo =individuo.imagen
		self.imagen=imagen
		self.sizeImage=sizeImage
		"""cv2.imshow("Real",self.individuo)
		cv2.imshow("individuo",self.imagen)
		cv2.waitKey(0)
		cv2.destroyAllWindows()	"""

	def calcularError(self):
		error = 0
		p=0
		for y in range(self.sizeImage):
			for x in range(self.sizeImage):
				resta = abs(self.imagen[y,x] - self.individuo[y,x])
				error = error+resta
				p+=1
		#print("Error "+str(error))
		return error



"""imagen = cv2.imread('imagen.jpg',0) 
imagen = cv2.resize(imagen,(300,300))
for i in range(4):
	ind = Individuo()
	ind.inicializar()
	f = Funcion(imagen,ind)
	f.calcularError()"""




