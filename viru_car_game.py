import pygame
import time
import random

pygame.init()
crash_sound = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("No_Culture.mp3")
display_width=700
display_height=600

black = (0,0,0)
white = (255,255,255)
red = (200 ,0, 0)
block_color = (53, 115, 255)
blue = (53 ,49 ,255)
green = (0,200,0)
bright_red = (255 ,0 ,0)
bright_green = (0 , 255 ,0)
purple = (163 , 73 ,164)

car_width = 99
pause=False

gamedisplay= pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A crazy car')

clock=pygame.time.Clock()
gameImg = pygame.image.load('gameImg.jpg')

carImg=pygame.image.load('racecar.png')

pygame.display.set_icon(carImg)

def things_dodged(count):
    font = pygame.font.SysFont(None , 24)
    text = font.render("Score: "+str(count), True, black)
    gamedisplay.blit(text,(10,0))
   
def things(thingx , thingy , thingw, thingh, color):
    pygame.draw.rect(gamedisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gamedisplay.blit(carImg,(x,y))

def gamecar(i,k):
    gamedisplay.blit(gameImg,(i,k))

def text_object(text , font):
    textsurface = font.render(text, True ,black)
    return textsurface, textsurface.get_rect()  #get_rect()->to get the rectangle that is somewhat invisible  

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf',50)  #Largetext used to define the fontstyle and fontsize of text. pygame.font.Font() #takes two argument (fontstyle,fontsize)
    textsurf, textrect = text_object(text, largetext) #text_object returns textsurf(text!) and the rectangle that would encompass it
    textrect.center = ((display_width/2),(display_height/2))  # .center is used to center the text 
    gamedisplay.blit(textsurf,textrect) # it will make of text format on the screen.
    pygame.display.update()
    time.sleep(2)   #as game is over the game is going to sleep mode for 2 second
    game_loop()



def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display('You Crashed')  #display the message on the screen

def button(msg,x,y,w,h,ic,ac,action = None):
    '''
    x: the location of the top left coordinate
    y: the location of y
    w:width of button
    h:height of button
    ic:inactuve color(when mouse is not hovering)
    ac:active color(when mouse is hovering
    action: what action is taken on clicking on button
    '''
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] >x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplay , ac ,(x , y ,w ,h))
        if click[0] == 1 and action !=None:
            action()
            
    else:
        pygame.draw.rect(gamedisplay , ic,(x , y ,w,h))
    smalltext = pygame.font.Font('freesansbold.ttf',20)  #Largetext used to define the fontstyle and fontsize of text. pygame.font.Font() #takes two argument (fontstyle,fontsize)
    textsurf, textrect = text_object(msg, smalltext) #text_object returns textsurf(text!) and the rectangle that would encompass it
    textrect.center = ((w/2+x),(h/2 + y))  # .center is used to center the text 
    gamedisplay.blit(textsurf,textrect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():
    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplay.fill(red)
        largetext = pygame.font.Font('freesansbold.ttf',50)  #Largetext used to define the fontstyle and fontsize of text. pygame.font.Font() #takes two argument (fontstyle,fontsize)
        textsurf, textrect = text_object("Paused", largetext) #text_object returns textsurf(text!) and the rectangle that would encompass it
        textrect.center = ((display_width/2),(display_height/2))  # .center is used to center the text 
        gamedisplay.blit(textsurf,textrect)

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",450,450,100,50,blue,block_color,quitgame)
        mouse = pygame.mouse.get_pos()
    

        pygame.display.update()
        clock.tick(10)

def game_intro():
    i = (display_width * 0.25)
    k = (0)
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplay.fill(red)
        gamecar(i,k)
        largetext = pygame.font.Font('freesansbold.ttf',50)  #Largetext used to define the fontstyle and fontsize of text. pygame.font.Font() #takes two argument (fontstyle,fontsize)
        textsurf, textrect = text_object("A crazy car crash", largetext) #text_object returns textsurf(text!) and the rectangle that would encompass it
        textrect.center = ((display_width/2),(display_height/2))  # .center is used to center the text 
        gamedisplay.blit(textsurf,textrect)

        button("Go!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",450,450,100,50,blue,block_color,quitgame)
        mouse = pygame.mouse.get_pos()
    

        pygame.display.update()
        clock.tick(10)

        
        

    
def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.7999)
   
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 10
    thing_width = 100
    thing_height = 100

    thingcount=1
    dodged = 0
    thing_block=1

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                if event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key == pygame.K_p:
                    pause=True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x +=x_change
            
        gamedisplay.fill(purple)
        car(x,y)
        things_dodged(dodged)
        temp = thing_startx
        if thing_block == 1:
            ll = 1
        for q in range(2):
            if q == 0:
                things(temp,thing_starty,thing_width,thing_height,block_color)
            elif q == 1:
                if ll == 1:
                    thing_startxx = random.randrange(0, display_width)
                    ll+=1
                    thing_block+=1
                things(thing_startxx,thing_starty,thing_width,thing_height,block_color)
                
                
        #things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty+=thing_speed
        #things_dodged(dodged)
        if x > display_width - car_width or x < 0:
            crash()  #when user touches the boundies it will be crased and game is over!
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            ll == 1
            dodged +=1
            thing_speed+=0.1
            thing_block = 1
            #thing_width +=(dodged * 1.2)

        if y< thing_starty+thing_height - 20:
            if x>thing_startx  and x < thing_startx + thing_width or x+car_width - 30> thing_startx and x + car_width   <thing_startx + thing_width:
                crash()
        if y< thing_starty+thing_height - 20:
            if x>thing_startxx  and x < thing_startxx + thing_width or x+car_width - 30> thing_startxx and x + car_width   <thing_startxx + thing_width:
                crash()
            
            
        pygame.display.update()

        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()
