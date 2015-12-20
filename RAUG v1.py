#@author Cj Maxwell
import turtle

def main():
    screen = turtle.Screen()
    screen.bgcolor('black')
    height, width = boxInScreen(screen)
    mainMenu(height, width)
    screen.onclick(chooseMenuItem)
    screen.mainloop()

def boxInScreen(screen):
    t = turtle.Turtle()
    t.color('grey', 'black')
    #t.fillcolor('')
    width = screen.window_width()
    height = screen.window_height()
    t.speed(0)
    t.pu()
    t.bk(width/2-40)
    t.rt(90)
    t.fd(height/2-40)
    t.lt(90)
    t.pd()
    t.begin_fill()
    for i in range(2):
        t.fd(width-80)
        t.left(90)
        t.fd(height-80)
        t.left(90)
    t.end_fill()
    t.pu()
    t.hideturtle()
    return(width-80, height-80)
    


def deul(player1hand,player2hand):
    pass

def drawCards(numcards):
    pass

def populateDeck():
    pass

def createPlayer(name):
    pass

def mainMenu(height, width):
    t = turtle.Turtle()
    t.color('yellow')
    t.pu()
    t.goto(-width/2,height/3)
    t.pd()
    menu = ["New Game",'Load Game', 'Game Options', 'Save Game', 'Save & Quit']
    t.write("Main Menu", font=("Monospace", 24, "bold"))
    print("mainmenu @ ", t.pos())
    t.up()
    t.fd(8)
    t.pd()
    levelsin = 1
    for menuitem in menu:
        levelsin += 1
        t.rt(90)
        t.fd(30)
        t.lt(90)
        t.fd(10+2*levelsin)
        t.write(menuitem[0], font=("Monospace", 16, "underline"))
        print(menuitem, " @ ", t.pos())
        t.pu()
        t.fd(20)
        t.write(menuitem[1:], font=("Monospace", 16, "normal"))
        t.pd()
        t.bk(10+2*levelsin)
    t.hideturtle()
    
    
def chooseMenuItem(x,y):
    if 293.33 > y > 233.33:
        print('New Game Selected')
    if 263.33 > y > 203.33:
        print('Load Game Selected')
    if 233.33 > y > 173.33:
        print('Game Options Selected')
    if 203.33 > y > 143.33:
        print('Save Game Selected')
    if 173.33 > y > 113.33:
        print('Save & Quit Selected')
#function calls
main()
