#@author Cj Maxwell
#@file: Runs main menu
#@description: pulls all aspects of game together
#@dependencies: _newgame_.py
#               _savegame_.py
#               _gameoptions_.py

import turtle
import winsound
import _newgame_
import tkinter

colors = ['grey', 'red']
x, y, z = 0, 1, 2
thatsannoying = False
currentmenu = "Main Menu"
menpos = {}

def main():
    global menpos
    screen = turtle.Screen()
##    cv = screen.getcanvas()
##    cv.pack(expand = 'yes', fill = 'both')
##    firegif1 = tkinter.PhotoImage(file = 'BurningFlame0.gif')
##    cv.create_image(50, 10, image = firegif1, anchor = 'nw')
    screen.setup(width=1., height=1.)
    screen.bgcolor('black')
    
    winsound.PlaySound('german_fire_siren_calls_fire_department_rain_in_ba.wav', winsound.SND_ASYNC)
    #screen.bgpic('Pentagram 2.png')
    color = 'gray'
    width, height = boxInScreen(screen, color)
    t = turtle.Turtle()
    menpos = mainMenu(width, height, screen, t)
    def getClickCoords(x,y):
        mainMenuActivator(x,y, width, height, screen, t)

    def flashScreen():
        global thatsannoying
        invertColors(screen)
        if not thatsannoying:
            screen.ontimer(flashScreen, 150)
        
    screen.ontimer(flashScreen, 1000)
    screen.onclick(getClickCoords)
    screen.mainloop()

def invertColors(screen):
    global x,y
    dummy1, dummy2 = boxInScreen(screen, colors[y])
    temp = x
    x=y
    y=temp
    

def boxInScreen(screen,color):
    t = turtle.Turtle()
    t.hideturtle()
    t.color(color,'black')
    width = screen.window_width()
    height = screen.window_height()
    t.speed(0)
    t.pu()
    t.bk(width/2-40)
    t.rt(90)
    t.fd(height/2-40)
    t.lt(90)
    t.pd()
    
    for i in range(2):
        t.fd(width-80)
        t.left(90)
        t.fd(height-80)
        t.left(90)
    t.pu()
    t.clear()
    return(width-80, height-80)
    
def mainMenuActivator(x,y, width, height, screen, t):
    global currentmenu, menpos

    def openNewGameMenu():
        menpos = _newgame_.newGameMenu(width, height, screen, t)
        _newgame_.passArgs(width, height, screen, t, currentmenu, menpos)
        screen.onclick(_newgame_.getClickCoords)
    def openLoadGameMenu():
        menpos = _loadgame_.newGameMenu(width, height, screen, t)
        _loadgame_.passArgs(width, height, screen, t, currentmenu, menpos)
        screen.onclick(_loadgame_.getClickCoords)
    def openGameOtionsMenu():
        menpos = _gameoptions_.newGameMenu(width, height, screen, t)
        _gameoptions_.passArgs(width, height, screen, t, currentmenu, menpos)
        screen.onclick(_gameoptions_.getClickCoords)
    def openSaveMenu():
        menpos = _savegame_.newGameMenu(width, height, screen, t)
        _savegame_.passArgs(width, height, screen, t, currentmenu, menpos)
        screen.onclick(_savegame_.getClickCoords)
    
    if currentmenu=='Main Menu':
        boxT = turtle.Turtle()
        boxT.color('yellow')
        menuitem = chooseMenuItem(x,y)
        winsound.PlaySound('spooky_film_theme_scary_yet_tension_building_theme.wav', winsound.SND_ASYNC)
        if menuitem in menpos:
            boxT.hideturtle()
            boxT.color('yellow')
            boxT.up()
            boxT.goto(menpos[menuitem][0]-20, menpos[menuitem][1])
            boxT.down()
            
            for i in range(2):
                boxT.fd(270)
                boxT.left(90)
                boxT.fd(45)
                boxT.left(90)
            boxT.reset()
            #print(menuitem)
            if 'Save' not in menuitem:
                t.reset()
                pass
            currentmenu = menuitem
            if currentmenu == 'New Game':
                openNewGameMenu()
            elif currentmenu == 'Load Game'
                openLoadGameMenu()
            elif currentmenu == 'Game Options'
                openGameOptionsMenu()
            elif currentMenu == 'Save Game'
                openSaveMenu()
            elif currentMenu == 'Save & Quit'
                _savegame_.quickSave()
                s.bye()
def deul(player1hand,player2hand):
    pass

def drawCards(numcards):
    pass

def populateDeck():
    pass

def createPlayer(name):
    pass

def mainMenu(width, height, screen, t):
    t.hideturtle()
    t.color('yellow')
    t.pu()
    t.goto(-width/2.5,height/3.25)
    t.pd()
    menu = ["New Game",'Load Game', 'Game Options', 'Save Game', 'Save & Quit']
    menpos = {}
    menpos["Main Menu"] = t.pos()
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
        t.write(menuitem[0], font=("Monospace", 24, "underline"))
        t.pu()
        t.fd(30)
        t.write(menuitem[1:], font=("Monospace", 24, "normal"))
        t.pd()
        t.bk(15+2*levelsin)
    t.hideturtle()
    return menpos
    

    
def chooseMenuItem(x,y):
    global thatsannoying,menpos
    selection = ''
    if menpos["Main Menu"][1] > y > menpos["New Game"][1]:
        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('New Game Selected')
        selection = 'New Game'
        thatsannoying = True
    elif menpos["New Game"][1] > y > menpos["Load Game"][1]:
        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('Load Game Selected')
        selection = 'Load Game'
        thatsannoying = True
    elif menpos["Load Game"][1] > y > menpos["Game Options"][1]:
        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('Game Options Selected')
        selection = 'Game Options'
        thatsannoying = True
    elif menpos["Game Options"][1] > y > menpos["Save Game"][1]:
        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('Save Game Selected')
        selection = 'Save Game'
        thatsannoying = True
    elif menpos["Save Game"][1] > y > menpos["Save & Quit"][1]:
        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('Save & Quit Selected')
        selection = 'Save & Quit'
        thatsannoying = True
    return selection

#function calls
main()
