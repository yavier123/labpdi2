#! /usr/bin/python

from SimpleCV  import Image, Camera, Display, time

import matplotlib.pyplot as plt

cam = Camera()
img = cam.getImage()

img.save("foto1.jpg")

time.sleep(2)

img2=cam.getImage()

img2.save("foto2.jpg")

time.sleep(2)

img3=cam.getImage()
  
escaladegris=img2.grayscale()
escaladegris.save("fotogray.jpg")

histograma=escaladegris.histogram()

plt.figure(1)

plt.plot(histograma)

plt.show() 
