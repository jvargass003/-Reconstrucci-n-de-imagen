#Importar librería cv2
import cv2

#Leer imagen
img = cv2.imread('imagen.jpg')
#Cambiar img a escala de grises
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img2 = cv2.resize(img2,(300,300)) 

#Analiza 81 pixeles grises
for fila in range (300):
    for columna in range (300):
        print("Color", "fila:", + fila, "columna", + columna, "=", str(img2[fila,columna]))

#Mostrar imagen
cv2.imshow('imagenGris',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()