#@author Cj Maxwell
import turtle

def main():
    screen = turtle.Screen()
    screen.setup(width=1., height=1.)
    screen.bgcolor('black')
    width, height = boxInScreen(screen)
    menpos = mainMenu(width, height)

    #print(menpos)

    def getClickCoords(x,y):
        chooseMenuItem(x,y,menpos)

    screen.onclick(getClickCoords)
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

def mainMenu(width, height):
    t = turtle.Turtle()
    t.color('yellow')
    t.pu()
    t.goto(-width/2.5,height/3.25)
    t.pd()
    menu = ["New Game",'Load Game', 'Game Options', 'Save Game', 'Save & Quit']
    menpos = {}
    menpos["Main Menu"] = t.pos()
    t.stamp()
    print('Main Menu', t.pos())
    t.write("Main Menu", font=("Monospace", 36, "bold"))
    
    t.up()
    t.fd(8)
    t.pd()
    levelsin = 1
    for menuitem in menu:
        levelsin += 1
        t.rt(90)
        t.fd(55)
        t.lt(90)
        t.fd(15+2*levelsin)
        menpos[menuitem] = t.pos()
        t.stamp()
        print(menuitem, t.pos())
        
        
        t.write(menuitem[0], font=("Monospace", 24, "underline"))
        
        t.pu()
        t.fd(30)
        t.write(menuitem[1:], font=("Monospace", 24, "normal"))
        t.pd()
        t.bk(15+2*levelsin)
    t.hideturtle()
    print(menpos)
    return menpos
    

    
def chooseMenuItem(x,y,menpos):
    print(x,y)
    if menpos["Main Menu"][1] > y > menpos["New Game"][1]:
        print('New Game Selected')
    elif menpos["New Game"][1] > y > menpos["Load Game"][1]:
        print('Load Game Selected')
    elif menpos["Load Game"][1] > y > menpos["Game Options"][1]:
        print('Game Options Selected')
    elif menpos["Game Options"][1] > y > menpos["Save Game"][1]:
        print('Save Game Selected')
    elif menpos["Save Game"][1] > y > menpos["Save & Quit"][1]:
        print('Save & Quit Selected')
#function calls
main()
