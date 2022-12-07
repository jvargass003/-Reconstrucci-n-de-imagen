import numpy as np
import random
from Individuo import Individuo
import cv2
import math
from Funcion import Funcion
from Seleccion import Seleccion
from Poblacion import Poblacion

class Evolucion:
	def __init__(self,imagen,size=300,sizeCircle=1000):
		self.sizeCircle=sizeCircle
		self.size = size
		self.imagen= imagen
		self.nuevaPob = []
		self.pob = Poblacion(self.size,self.sizeCircle)
		self.pob.inicializa()
		self.errores = []
		self.idxSelec =[]


		self.generacion=0
		while(1):
			self.nuevaPob = []
			self.errores = []
			self.idxSelec =[]
			self.evolucionar()



	def evolucionar(self):
		print("Generacion "+str(self.generacion))
		
		#print(len(self.pob.poblacion))
		for i in range(self.size):
			f = Funcion(self.imagen,self.pob.poblacion[i])
			self.errores.append(f.calcularError())
		#print("Errores: ",(self.errores))
		#Seleccionar
		selec = Seleccion(self.errores,self.size)
		self.idxSele = selec.seleccionar()
		#print(self.idxSele)

		#Mostrar mejor individuo de esa población
		#print(len(self.pob.poblacion))
		self.pob.poblacion[self.idxSele[0]].decodificar()
		if (self.generacion%15 == 0 or self.generacion==0): cv2.imwrite("generacion "+str(self.generacion)+".jpg",self.pob.poblacion[self.idxSele[0]].imagen)
		cv2.imshow("generacion "+str(self.generacion),self.pob.poblacion[self.idxSele[0]].imagen)
		cv2.waitKey(1)
		cv2.destroyAllWindows()
		for n in range(int(self.size/2)):
			self.nuevaPob.append(self.pob.poblacion[self.idxSele[n]])
		#Cruzar
		for m in range(0,int((self.size/2)),2):
			hijo1, hijo2 = self.pob.poblacion[self.idxSele[m]].cruza(self.pob.poblacion[self.idxSele[m+1]])
			self.nuevaPob.append(hijo1)
			self.nuevaPob.append(hijo2)
		

		#mutación
		cadMutar = math.ceil(self.size*0.05)
		for muta in range(cadMutar):
			idx = (random.randint(0,self.size-1))
			self.pob.poblacion[idx].mutacion()


		self.pob.setPoblacion(self.nuevaPob)
		self.generacion += 1

imagen = cv2.imread('imagen.jpg',0)
imagen = cv2.resize(imagen,(300,300)) 
e = Evolucion(imagen)
e.evolucionar()




