#! /usr/bin/python

from SimpleCV  import Image, Camera, Display, time

import matplotlib.pyplot as plt


cam = Camera()

time.sleep(1)

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

plt.stem(histograma)

plt.grid()
  
plt.savefig('histogramaengris.png')

time.sleep(1)

#imgsplit= cam.getImage()

(red, green, blue) = img2.splitChannels(False)
 
red_histogram= red.histogram(255)

plt.figure(2)

plt.grid()

plt.stem(red_histogram)

plt.savefig('histogramaenrojo.png')

blue_histogram = blue.histogram(255)

plt.figure(3)

plt.stem(blue_histogram)

plt.savefig('histogramaenazul.png')

green_histogram= green.histogram(255)

plt.figure(4)

plt.stem(green_histogram)

plt.savefig('histogramaenverde.png')



