from random import *
y=450
Xspeed= 100
z=1
def setup():
    frameRate(30)
    size(500,500)
    background(0,0,0)
    fill(255,255,255)
    rect(195,220,150,50,10)
    fill(0,255,0)
    textSize(26)
    text("Welcome to Space Invaders", 100,200)
    textSize(13)
    fill(0,255,0)
    text("Double Click to Begin", 200,250)
Gameover = False
Invaders = False
Game = False
Player = False
Aliens = True
Shot = False
Aliensx = [50,100,150,200,250,300,350,400,450]
Aliensy = [50,100,150,200,250]
Killed_Aliens = []
Bullets = []

x = 0
def keyPressed():
    global Xspeed
    if key == "a":
        Xspeed -= 30
    elif key=="d":
        Xspeed+=30
def draw():
    global y
    global x
    global z
    global Aliensx
    global Aliensy
    global Aliens
    global Game
    global Invadersy
    global Invadersx
    global Shot
    if Gameover == False:
        if mouseX < 350 and mouseY < 380 and mouseX > 200 and mouseY > 220 and Game == False:
            if mousePressed and mouseButton == LEFT:
                background(0,0,0)
                Game = True
            background(0, 0, 0)
            fill(0,0,255)
            rect(Xspeed,450,25,25)                        
    
            def keyPressed():
                global Xspeed             
                if Player == True:
                    if key == "a":
                        if Xspeed >= 0:
                            Xspeed -= 10
                            Player = False
                    elif key=="d":
                        if Xspeed <= 500:
                            Xspeed+=10
                            Player = False

                                    
        if Game == True and Xspeed > 10 and Xspeed < 490:
            background(0, 0, 0)
            fill(0,0,255)
            rect(Xspeed,450,25,25)
            if Aliens == True:
                for i in range(len(Aliensx)):
                    Invadersx = (Aliensx[i])
                    for j in range(len(Aliensy)):
                        Invadersy = (Aliensy[j])
                        fill(255,255,255)
                        rect(Invadersx,x + i,25,25)
                for i in range(len(Aliensx)):
                    Invadersx = (Aliensx[i])
                    for j in range(len(Aliensy)):
                        Invadersy = (Aliensy[j])
                        fill(255,255,255)
                        rect(Invadersx,x + i + 50,25,25)
                for i in range(len(Aliensx)):
                    Invadersx = (Aliensx[i])
                    for j in range(len(Aliensy)):
                        Invadersy = (Aliensy[j])
                        fill(255,255,255)
                        rect(Invadersx,x + i + 100,25,25)
                for i in range (1):
                    rect(Invadersx,x + i,0,0)
                    x= x+0.5
                    if x + 1 > 500:
                        fill(255,255,255)
                        text("Gameover",250,250)   
            if mousePressed and mouseButton==LEFT and Game==True:
                fill(255,0,0)
                global Bulletx
                Bulletx = Xspeed
                global Bulletx
                ellipse(Bulletx + 12.5, y,10,10) 
                y = y - 30
                if y < 0:
                    y=450
                    fill(255,0,0)
                    ellipse(Bulletx + 12.5, y,10,10)        
            if Bulletx <= (Invadersx + 50) and Bulletx >= Invadersx and y<=Invadersy and Shot == True: 
                Aliensx.remove(450)
                Shot = False
    
                
"""                        
                                                                        
    

 IF we want to make it random later           
            for i in range(len(Aliensx)):
                x = randint(0,i)
                Invadersx = (Aliensx[x])
                for j in range(len(Aliensy)):
                    y = randint(0,j)
                    Invadersy = (Aliensy[y])
                    fill(255,255,255)
                    rect(Invadersx,Invadersy,25,25)
"""                    
