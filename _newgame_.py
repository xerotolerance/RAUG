#@author Cj Maxwell
#@file: Runs tasks related to starting a new game
import turtle
import winsound

def newGameMenu(width, height, screen, t):
    player_name = screen.textinput("Discover yourself: ", "And you would be... ")
    t.hideturtle()
    t.color('brown')
    t.pu()
    t.goto(width/3.25,height/3.25)
    t.pd()
    menu = ["Build Deck",'Build Stats', 'Trade Goods', 'Save Game', 'Save and Quit']
    menpos = {}
    menpos["Player Menu"] = t.pos()
    t.up()
    t.write("Player Menu", move = True, font=("Monospace", 36, "bold"))
    t.rt(180)
    t.fd(8)
    t.pd()
    levelsin = 1
    for menuitem in menu:
        levelsin += 1
        t.lt(90)
        t.fd(55)
        t.rt(90)
        t.fd(250+6*levelsin)
        menpos[menuitem] = t.pos()        
        t.write(menuitem[0], font=("Monospace", 24, "underline"))
        t.pu()
        t.bk(30-levelsin)
        t.write(menuitem[1:], move = True, font=("Monospace", 24, "normal"))
        t.pd()
        t.bk(20-3*levelsin)
    t.hideturtle()
    return menpos

def chooseMenuItem(x,y, menpos):
    global thatsannoying
    selection = ''
    if menpos["Player Menu"][1] > y > menpos["Build Deck"][1]:
        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        print('Build Deck Selected')
        selection = 'Build Deck'
        thatsannoying = True
    elif menpos["Build Deck"][1] > y > menpos["Build Stats"][1]:
        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        print('Build Stats Selected')
        selection = 'Build Stats'
        thatsannoying = True
    elif menpos["Build Stats"][1] > y > menpos["Trade Goods"][1]:
        winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        print('Trade Goods Selected')
        selection = 'Trade Goods'
        thatsannoying = True
    elif menpos["Trade Goods"][1] > y > menpos["Save Game"][1]:
        #winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        print('Save Game Selected')
        selection = 'Save Game'
        thatsannoying = True
    elif menpos["Save Game"][1] > y > menpos["Save and Quit"][1]:
        #winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
        print('Save and Quit Selected')
        selection = 'Save and Quit'
        thatsannoying = True
    return selection

args={}
def passArgs(width, height, screen, t, currentmenu, menpos):
    global args
    args = {'width': width, 'height':height, 'screen':screen,
            't': t, 'currentmenu':currentmenu, 'menpos':menpos}
def getClickCoords(x,y):
        newGameMenuActivator(x,y, args['width'], args['height'], args['screen'], args['t'], args['currentmenu'], args['menpos'])
        
def newGameMenuActivator(x,y, width, height, screen, t, currentmenu, menpos):
    #t = t.clone()
    boxT = turtle.Turtle()
    boxT.color('brown')
    if currentmenu =='New Game':
        menuitem = chooseMenuItem(x,y,menpos)
        if menuitem in menpos:
            print('menuitem clicked: ', menuitem)
            boxT.hideturtle()
            boxT.st()
            boxT.color('gray')
            boxT.up()
            boxT.goto(menpos[menuitem][0]-20+270, menpos[menuitem][1])
            boxT.down()
            
            for i in range(2):
                boxT.fd(270)
                boxT.rt(90)
                boxT.fd(45)
                boxT.rt(90)
            boxT.reset()
            t.reset()
            if 'Save' not in menuitem:
                t.reset()
            currentmenu = menuitem
