 # import the necessary packages
from SimpleCV import*#paquetes necesarios para trabajar , ocupamos el m'*' para facitar el trabajo
from sklearn.cluster import MiniBatchKMeans #con mini batch k means hacemos los kmeans necesario para trabajar , trbaajosmos con 2 que es la
import matplotlib.pyplot as plt # como vamos a trabajar con graficas importamos la bibloteca de librerias 
import numpy as np
import cv2 
import argparse
opcion = int(input("\nMenu\n--------------\n\t" + "1.Tomar foto\n\t "+"2.Kmeans\n\t"+"3.Segmentacion manual\n\t"+" 4.Exit "));

while(opcion !=4):
    
           if(opcion==1):
            print "Se toma la foto "
            cam= Camera()
            time.sleep(20)
            asdf=cam.getImage()
            asdf.save("experimento.jpg")
            # construct the argument parser and parse the arguments
            del cam
           elif(opcion==2):
            print "Algoritmo k-Means 2"
            # load the image and grab its width and height
            image = cv2.imread("experimento.jpg")
            (h, w) = image.shape[:2]
            image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
            image = image.reshape((image.shape[0] * image.shape[1], 3))
            clt = MiniBatchKMeans(2)#se aplica el numero de clusters
            labels = clt.fit_predict(image)
            quant = clt.cluster_centers_.astype("uint8")[labels]
            quant = quant.reshape((h, w, 3))
            image = image.reshape((h, w, 3))
            quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
            image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)
            cv2.imshow("image", np.hstack([image, quant]))
            cv2.waitKey(0)
           elif(opcion==3):
             print("Segmentacion manual")
             prueba=Image("experimento.jpg")
             escalagris=prueba.grayscale()
             escalagris.save("gray.jpg")
             histograma=escalagris.histogram(255)
             plt.subplot(4,1,1)
             plt.plot(histograma)
             plt.grid()
             plt.title("Histograma Grayscale cuadriculado")
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
             #se muestran en pantalla todo los histogramas en una misma grafica
             imgbin = escalagris.binarize(127)
             imgbin.save("imgbinarizada.jpg")
             imgbin2 = escalagris.binarize(170)
             imgbin2.save("imgbinarizada2.jpg")
             imgbin3=imgbin.invert()
             imgbin3.save("imagenbinarizadainvertida.jpg")
             imgbin4=imgbin2-imgbin
             imgbin4.save("imagenbinarizadaparaverelfondo.jpg")
             imgbin5=escalagris.binarize(20)
             imgbin5.save("Imagenprueba.jpg")
           elif(opcion==4):
             break
           else:
                print("ingresar opcion valida")
           opcion = int(input("\nMenu\n--------------\n\t" + "1.Tomar foto\n\t "+"2.Kmeans\n\t"+"3.Segmentacion manual\n\t"+" 4.Exit "));
    
print "exit"
