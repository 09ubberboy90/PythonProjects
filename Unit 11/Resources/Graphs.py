from Resources import Canvas
from random import randint
def scaling(inlist,ysize,xsize):
    global n
    maxim = largest(inlist)
    scalar = ysize/maxim
    xbar = xsize/len(inlist)
    for num,el in enumerate(inlist):
        inlist[num] = el * scalar
    return inlist,xbar

def largest(inlist):
    tmp = 0 #creates a tuple with left being the index and right the number
    for el in inlist:
        if el>tmp:
            tmp = el
    return tmp
def rectangle(inlist,xwidth,xOrigin,yOrigin):
    color = ["black", "white", "red", "blue", "green", "yellow", "cyan", "magenta"]
    for num,el in enumerate(inlist):
        yTop = yOrigin - el
        xTop = xOrigin + xwidth
        Canvas.create_rectangle(xOrigin, yOrigin, xTop, yTop, fill=color[num%len(color)])
        xOrigin += xwidth
def label(inlist,xwidth,xOrigin,yOrigin):
    for el in inlist:
        yCenter = yOrigin + 10
        xCenter = xOrigin + xwidth/2
        Canvas.create_text(xCenter, yCenter, text=el)
        xOrigin += xwidth
def line(xOrigin,yOrigin,xSize,ySize,maxim):
    scalar = ySize/int(maxim)
    Canvas.create_line(xOrigin, yOrigin, xOrigin+xSize, yOrigin)
    Canvas.create_line(xOrigin, yOrigin, xOrigin, yOrigin-ySize)    
    for i in range(int(maxim)+1):
        Canvas.create_line(xOrigin-5, yOrigin-i*scalar, xOrigin+5, yOrigin-i*scalar)
        Canvas.create_text(xOrigin-20, yOrigin-i*scalar, text=i)
    
def barchart(xOrigin,yOrigin,xSize,ySize,labels,data):
    maxim = largest(data)
    Canvas.set_size(xSize+xOrigin,ySize+yOrigin+50)
    yOrigin = ySize - yOrigin+50
    newlist = scaling(data, ySize, xSize)[0]
    xwidth = scaling(data, ySize, xSize)[1]
    rectangle(newlist, xwidth,xOrigin,yOrigin)
    label(labels, xwidth, xOrigin, yOrigin)
    line(xOrigin,yOrigin,xSize,ySize,maxim)
def randomize(number):
    ls = ([],[])
    for i in range(number):
        ls[0].append(i+1)
        ls[1].append(randint(0,100))
    return ls
#barchart(30,20,550,300, randomize(20)[0], randomize(20)[1])
#barchart(30,20,1300,700, randomize(100)[0], randomize(100)[1])
#complete()