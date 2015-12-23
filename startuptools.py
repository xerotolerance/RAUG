#@author Cj Maxwell
#@file: Runs main menu
#@description: pulls all aspects of game together
#@dependencies: playermenutools.py
#               loadtools.py
#               gameoptions.py
#               savetools.py


import turtle
import winsound

import playermenutools
import loadtools
import gameoptions
import savetools
import tkinter

colors = ['grey', 'red']
x, y, z = 0, 1, 2
thatsannoying = False
previousmenu = ""
currentmenu = "Main Menu"
menpos = {}

def main():
    global menpos
    screen = turtle.Screen()

    screen.setup(width=1., height=1.)
    screen.bgcolor('black')
    
    color = 'gray'
    outT = turtle.Turtle()
    width, height = boxInScreen(screen, color, '', True, outT)
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


def playSiren():
    global currentmenu
    print(currentmenu)
    if currentmenu == 'Main Menu':
        winsound.PlaySound('german_fire_siren_calls_fire_department_rain_in_ba.wav', winsound.SND_ASYNC)

def playSpooky1():
    global currentmenu
    print(currentmenu)
    if currentmenu == 'New Game':
        winsound.PlaySound('spooky_film_theme_scary_yet_tension_building_theme.wav', winsound.SND_ASYNC)


def invertColors(screen):
    global x,y
    t = turtle.Turtle()
    dummy1, dummy2 = boxInScreen(screen, colors[y], '', True, t)
    temp = x
    x=y
    y=temp
    

def boxInScreen(screen,color,fillcolor, remove_artifacts, t):
    t.hideturtle()
    t.color(color,fillcolor)
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
    if remove_artifacts:
        t.clear()
    return(width-80, height-80)
    
def mainMenuActivator(x,y, width, height, screen, t):
    global currentmenu, previousmenu, menpos

    def openNewGameMenu():
        menpos = playermenutools.newGameMenu(width, height, screen, t)
        playermenutools.passArgs(width, height, screen, t, currentmenu,previousmenu, menpos)
        screen.onclick(playermenutools.getClickCoords)
    def openLoadGameMenu():
        menpos = loadtools.loadGameMenu(width, height, screen, t)
        loadtools.passArgs(width, height, screen, t, currentmenu,previousmenu, menpos)
        screen.onclick(loadtools.getClickCoords)
    def openGameOtionsMenu():
        menpos = gameoptions.gameOptionsMenu(width, height, screen, t)
        gameoptions.passArgs(width, height, screen, t, currentmenu,previousmenu, menpos)
        screen.onclick(gameoptions.getClickCoords)
    def openSaveMenu():
        menpos = savetools.saveGameMenu(width, height, screen, t)
        savetools.passArgs(width, height, screen, t, currentmenu,previousmenu, menpos)
        screen.onclick(savetools.getClickCoords)
    
    if currentmenu=='Main Menu':
        boxT = turtle.Turtle()
        boxT.hideturtle()
        boxT.color('yellow')
        menuitem = chooseMenuItem(x,y)
        
        if menuitem in menpos:
            if 'Save' not in menuitem:
                screen.ontimer(playSpooky1, 36999)
                winsound.PlaySound('spooky_film_theme_scary_yet_tension_building_theme.wav', winsound.SND_ASYNC)
            if 'Quit' in menuitem:
                winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
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
                
            currentmenu = menuitem
            if currentmenu == 'New Game':
                openNewGameMenu()
            elif currentmenu == 'Load Game':
                openLoadGameMenu()
            elif currentmenu == 'Game Options':
                openGameOptionsMenu()
            elif currentmenu == 'Save Game':
                openSaveMenu()
            elif currentmenu == 'Save & Quit':
                savetools.quickSave(width, height)
                screen.bye()
def deul(player1hand,player2hand):
    pass

def drawCards(numcards):
    pass

def populateDeck():
    pass

def createPlayer(name):
    pass

def mainMenu(width, height, screen, t):
    screen.ontimer(playSiren, 87997)
    winsound.PlaySound('german_fire_siren_calls_fire_department_rain_in_ba.wav', winsound.SND_ASYNC)
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
##        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('New Game Selected')
        selection = 'New Game'
        thatsannoying = True
    elif menpos["New Game"][1] > y > menpos["Load Game"][1]:
##        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('Load Game Selected')
        selection = 'Load Game'
        thatsannoying = True
    elif menpos["Load Game"][1] > y > menpos["Game Options"][1]:
##        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('Game Options Selected')
        selection = 'Game Options'
        thatsannoying = True
    elif menpos["Game Options"][1] > y > menpos["Save Game"][1]:
##        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('Save Game Selected')
        selection = 'Save Game'
        thatsannoying = True
    elif menpos["Save Game"][1] > y > menpos["Save & Quit"][1]:
##        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        #print('Save & Quit Selected')
        selection = 'Save & Quit'
        thatsannoying = True
    return selection

#function calls
main()
