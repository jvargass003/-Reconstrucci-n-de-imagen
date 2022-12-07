import numpy as np
import random
import cv2
from Circulo import Circulo
class Individuo:
 	def __init__(self,size=1000,sizeIma=300):
 		self.cromosoma = []
 		self.size = size
 		self.sizeIma = sizeIma

 	def inicializar(self):
 		for i in range(self.size):
 			circle = Circulo()
 			self.cromosoma.append(circle)

 	def decodificar(self):
 		self.imagen = 255*np.ones((self.sizeIma,self.sizeIma),dtype=np.uint8)
 		for c in range(self.size):
 			cv2.circle(self.imagen,self.cromosoma[c].posicion,self.cromosoma[c].radio,self.cromosoma[c].tono,-1)

 	def getCromosoma(self):
 		return self.cromosoma

 	def setCromosoma(self,cromosoma):
 		self.cromosoma = cromosoma
 	def cruza(self, madre):
 		#Realizamos una divisiónde la imagen
 		mitad = int(self.size/2)
 		hijo1= []
 		hijo2= []

 		padre = self.cromosoma
 		madre = madre.cromosoma

 		hijo1 = padre[:mitad]+madre[mitad:] 
 		hijo2 = padre[mitad:]+madre[:mitad]
 		h1 = Individuo(self.size)
 		h2 = Individuo(self.size)
 		h1.setCromosoma(hijo1)
 		h2.setCromosoma(hijo2)

 		return [h1,h2]

 	def mutacion(self):
 		idx = (random.randint(0,self.size-1))
 		circle = Circulo()
 		self.cromosoma[idx]= circle



#Pruebas
"""padre = Individuo(20)
padre.inicializar()
madre = Individuo(20)
madre.inicializar()
hijo1, hijo2 = padre.cruza(madre)

madre.decodificar()
padre.decodificar()
hijo1.decodificar()
hijo2.decodificar()


cv2.imshow("madre",madre.imagen)
cv2.imshow("padre",padre.imagen)
cv2.imshow("hijo1",hijo1.imagen)
cv2.imshow("hijo2",hijo2.imagen)


madre.mutacion()
madre.decodificar()
cv2.imshow("mutacion",madre.imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()	

"""