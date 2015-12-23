#@author Cj Maxwell
#@file: Runs tasks related to starting a new game
import turtle
import winsound
#import startuptools

saveboxT = turtle.Turtle()
saveboxT.ht()
saveboxT.pu()

def saveGameMenu(width, height, screen, t):
    global saveboxT
    #player_name = screen.textinput("Discover yourself: ", "And you would be... ")
    outT = turtle.Turtle()
    outT.ht()

    saveboxT = boxInSaveMenu(screen,'silver','red',False, outT)
    menpos = {'exitbox_bottom_left':saveboxT.pos()}

    t.hideturtle()
    t.color('black')
    t.pu()
    t.goto(-150,menpos['exitbox_bottom_left'][1]-15)
    #t.home()
    t.pd()
    menu = ['Slot 1','Slot 2', 'Slot 3']
    
    menpos["Save Game"] = t.pos()
    #t.stamp()
    t.up()
    t.bk(30)
    t.write("Save Game", move = True, font=("Monospace", 36, "bold"))
    t.rt(180)
    t.fd(8)
    t.pd()
    levelsin = 1
    for menuitem in menu:
        #levelsin += 1
        t.lt(90)
        t.fd(110)
        t.rt(90)
        t.fd(250+6*levelsin)
        menpos[menuitem] = t.pos()
        #t.stamp()
        t.write(menuitem[0], font=("Monospace", 24, "underline"))
        t.pu()
        t.bk(30-levelsin)
        t.write(menuitem[1:], move = True, font=("Monospace", 24, "normal"))
        t.pd()
        t.bk(150)
    t.hideturtle()
    return menpos

def chooseMenuItem(x,y, menpos):
    global thatsannoying
    selection = ''
    if menpos["Save Game"][0] < x < menpos["Save Game"][0] + 256:
        if menpos["Save Game"][1] > y > menpos["Slot 1"][1]: 
            winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
            print('Slot 1 Selected')
            selection = 'Slot 1'
            thatsannoying = True
        elif menpos["Slot 1"][1] > y > menpos["Slot 2"][1]:   
            winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
            print('Slot 2 Selected')
            selection = 'Slot 2'
            thatsannoying = True
        elif menpos["Slot 2"][1] > y > menpos["Slot 3"][1]:        
            winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
            print('Slot 3 Selected')
            selection = 'Slot 3'
            thatsannoying = True
    elif  menpos['exitbox_bottom_left'][1] + 60 > y > menpos['exitbox_bottom_left'][1]:
        if menpos['exitbox_bottom_left'][0] < x < menpos['exitbox_bottom_left'][0] + 60:
            winsound.PlaySound('silence.wav', winsound.SND_FILENAME)
            print('Exit Box Selected')
            selection = 'exitbox_bottom_left'
        thatsannoying = True
    return selection

args={}
def passArgs(width, height, screen, t, currentmenu, previousmenu, menpos):
    global args
    args = {'width': width, 'height':height, 'screen':screen,
            't': t, 'currentmenu':currentmenu, 'previousmenu':previousmenu, 'menpos':menpos}
def getClickCoords(x,y):
        saveGameMenuActivator(x,y, args['width'], args['height'], args['screen'], args['t'], args['currentmenu'], args['previousmenu'], args['menpos'])
        
def saveGameMenuActivator(x,y, width, height, screen, t, currentmenu, previousmenu, menpos):
    #t = t.clone()
    boxT = turtle.Turtle()
    boxT.hideturtle()
    boxT.color('brown')

    def saveTo(slotnum):
        pass

    if currentmenu =='Save Game':
        menuitem = chooseMenuItem(x,y,menpos)
        if menuitem in menpos:
            print('menuitem clicked: ', menuitem)
            
            boxT.st()
            boxT.color('gray')
            boxT.up()
            boxT.goto(menpos[menuitem][0]-20+270, menpos[menuitem][1])
            boxT.lt(180)
            boxT.width(10)
            boxT.down()
            
            for i in range(2):
                boxT.fd(270)
                boxT.rt(90)
                boxT.fd(45)
                boxT.rt(90)
            boxT.reset()
            
            if 'Slot' in menuitem:
                saveTo(menuitem)
            saveboxT.reset()
            currentmenu = previousmenu
            previousmenu = 'Save Game'
        if currentmenu == 'Main Menu':
            #startuptools.main()
            pass
            
def quickSave(width, height):
    t = turtle.Turtle()
    t.color('yellow', 'gray')
    t.pu()
    t.bk(width/2)
    t.lt(90)
    t.begin_fill()
    for i in range(2):
        pass
    t.end_fill()
    t.write('GAME SAVED', move = True)
    print('GAME SAVED')


def boxInSaveMenu(screen,color,fillcolor, remove_artifacts, t):
    print('outline color: ' + color + ', fillcolor: ' + fillcolor)
    t.speed(0)
    t.hideturtle()
    t.color(color,fillcolor)
    t.width(15)
    width = screen.window_width() / 2
    height = screen.window_height() / 2

    t.speed(5)
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
    t.lt(90)
    t.fd(height-100)
    t.rt(90)
    t.fd(20)
    t.pd()
    t.color('brown')
    t.width(15)
    for i in range(4):
        t.fd(60)
        t.rt(90)
    t.rt(45)
    t.fd(60*2**.5)
    t.lt(135)
    t.fd(60)
    t.lt(135)
    t.fd(60*2**.5)
    t.lt(135)
    if remove_artifacts:
        t.clear()
    return t
