#@Author: CJ Maxwell
#@Product Name: RAUG [Really, Another Useless Game?]
#@Description: Animated Battle Card Game

from turtle import *
import random
colors = ['red','green','blue', 'pink', 'black', 'orange', 'yellow', 'purple', 'gray']

def gameWindow():
    cellsize = 500
    s = Screen()
    boxt = Turtle()
    boxt.speed(0)
    boxt.hideturtle()
    
    def centerBox(t,size):
        t.width(10)
        t.up()
        t.bk(size/2)
        t.left(90)
        t.bk(size/2)
        t.right(90)
        t.down()

    def drawBoxes(num_of_boxes):
        print("drawing ", num_of_boxes, " boxes")

        def drawBox(size):
            for i in range(4):
                s.bgcolor(colors[random.randint(0,len(colors)-1)])
                for j in range(len(colors)):
                    chosen_color = colors[random.randint(0,len(colors)-1)]
                    boxt.color(chosen_color)
                    boxt.fd(size/len(colors))
                    boxt.left(90)
                    boxt.fd(size/9)
                    boxt.bk(size/9)
                    boxt.right(90)
                boxt.left(90)

        centerBox(boxt, cellsize)
        for i in range(num_of_boxes):
            drawBox(cellsize*((9-2*i)/9))
            boxt.up()
            boxt.fd(cellsize/(9))
            boxt.left(90)
            boxt.fd(cellsize/(9))
            boxt.right(90)
            boxt.down()
    
    drawBoxes(5)
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-8,-4)
    t.down()
    t.write('GO!')
    t.fd(22)
    s.bgcolor(colors[random.randint(0,len(colors)-1)])
def mainMenu():
    pass

gameWindow()
