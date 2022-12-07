import numpy as np
import random

class Circulo:
	def __init__(self):
		self.posicion = (random.randint(0,300),random.randint(0,300))
		self.radio = (random.randint(1,15))
		self.tono = (random.randint(0, 255))
