from random import *
value = 0
def setup():
    size(490,700)
    background(255,255,255)
    fill (255,0,0)
    rect(0,0,70,70)
    fill (255,128,0)
    rect(70,0,70,70)
    fill (255,255,0)
    rect(140,0,70,70)
    fill (0,255,0)
    rect(210,0,70,70)
    fill (0,0,255)
    rect(280,0,70,70)
    fill (255,0,255)
    rect(350,0,70,70)
    fill (0,0,0)
    rect(420,0,70,70)
    fill(255,255,255)
    stroke(255,255,255)
    fill(0,0,0)
    text("circle",10,500,490/3, 490/3)
def draw():
    a = 3
    x = randint(0,256)
    y = randint(0,256)
    z = randint(0,256)
    if mouseButton == LEFT:
        if mouseX < 70 and mouseY < 70:
            fill (255,0,0)
            stroke (255,0,0)
        elif mouseX < 140 and mouseX > 70 and mouseY < 70:
            fill (255,128,0)
            stroke (255,128,0)
        elif mouseX < 210 and mouseX > 140 and mouseY < 70:
            fill (255,255,0)
            stroke (255,255,0)
        elif mouseX < 280 and mouseX > 210 and mouseY < 70:
            fill (0,255,0)
            stroke (0,255,0)
        elif mouseX < 350 and mouseX > 280 and mouseY < 70:
            fill (0,0,255)
            stroke (0,0,255)
        elif mouseX < 420 and mouseX > 350 and mouseY < 70:                
            fill (255,0,255)
            stroke (255,0,255)
        elif mouseX < 490 and mouseX > 420 and mouseY < 70:                
            fill (0,0,0)
            stroke (0,0,0)
    if mouseButton == RIGHT:
                fill(x,y,z)
                stroke(x,y,z)
                ellipse(mouseX,mouseY,10,10)
    if mousePressed == True:
            if mouseY > 70:
                ellipse(mouseX,mouseY,10,10)