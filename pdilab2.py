#! /usr/bin/python
#TODA  LAS FOTOS DEBEN TENER EL MISMO TEXTO ESCRITO SOLO SE CAMBIARA LA SUPERFICI
#DEL TEXTO
from SimpleCV  import Image, Camera, Display, time 
import matplotlib.pyplot as plt
cam = Camera()
asdf=cam.getImage()
time.sleep(2)
prueba=cam.getImage()
prueba.save("prueba1.jpg")
escalagris=prueba.grayscale()
escalagris.save("gray.jpg")
histograma=escalagris.histogram()
plt.subplot(4,1,1)
plt.plot(histograma)
plt.grid()
plt.title("Histograma Grayscale")
#una vez echo el filtro en gris se procede a hacerlo en RGB(RED GREEn BLUE)
(red,green,blue)=prueba.splitChannels(False)
red_histogram=red.histogram(255)
plt.subplot(4,1,2)
plt.plot(red_histogram)
plt.grid()
plt.title("Histograma red")
green_histogram=green.histogram(255)
plt.subplot(4,1,3)
plt.plot(green_histogram)
plt.grid()
plt.title("Histograma green")
blue_histogram=blue.histogram(255)
plt.subplot(4,1,4)
plt.plot(blue_histogram)
plt.grid()
plt.title("Histograma blue")
plt.savefig("Todo los histogramas")
plt.show()
#se muestran en pantalla todo los histogramas en una misma grafica 









