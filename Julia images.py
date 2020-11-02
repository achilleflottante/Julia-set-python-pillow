
from PIL import Image
from math import cos,sin,radians
import os

os.system("rm /Users/achille/Desktop/images/*")


dim = 256
frames  = []

def generate_julia(dim, sizex, sizey, centerx, centery, number,c):

    image = Image.new('HSV',(dim,dim))
    pixels = image.load()

    for y in range(dim):
        for x in range(dim):
            truex = x-(dim/2)
            truey = y-(dim/2)
            z = complex(truex*(sizex/dim)+centerx,truey*(sizey/dim)+centery)
            counter = 0
            while abs(z) < 2 and counter < 1000:
                z = z**2 + c
                counter += 1
            if abs(z) < 2:
                pixels[x,y] = (0,0,0)
            else:
                hue = (counter)%360
                saturation =300
                value = 300
                color = (hue,saturation,value)
                #color = (255-(counter*2)%255, 255- (counter*2)%255, 255 )

                pixels[x,y] = color
    image = image.convert(mode='RGB')
    return image




truedim = 2.2
centerx = 0
centery = 0

c = complex(0.26,0)

rcos = 0.008
rsin = 0.005
angle = 0
c = complex(0.26+rcos * cos(radians(angle)), rsin * sin(radians(angle)))


for i in range(36):
    image = generate_julia(dim, truedim, truedim, centerx, centery, i, c)
    image.save(f'/Users/achille/Desktop/images/{i}.jpg')
    frames.append(image)
    print(i)
    c = complex(0.26+rcos * cos(radians(angle)), rsin * sin(radians(angle)))
    angle +=10

frames[0].save('yourfolder', save_all=True, append_images = frames[1:],duration=100, loop=0)
