from random import *
def setup():
    size(500,500)
    background(25,320,120)
x = 250
y = 250
a = False
b = False
c = False
count = 0
z = 10
def draw():
    global x
    global y
    global z
    global a 
    global b
    global count
    background(0,0,0)    
    fill(255, 210, 230)
    ellipse(x,y,45,45)
    if mouseButton == LEFT:
        if a == False:
            x += 6
            y += 1
            if x > 475:
                a = True
        elif a == True:
            x -= 4
            y += 4
            if x < 25:
                a = False
        if b == False:
            x += 4
            y += 8
            if y > 475:
                b = True
        elif b == True:
            x += 1
            y -= 5
            if y < 25:
                b = False
    rect(mouseX-50,450,z**2,z)
    if x > mouseX-50 and x < mouseX+50 and y > 440 :
        if c == False:
            b = True
            count += 1
    if y >= 450:
        fill(255,255,255)
        textSize(50)
        text("Game Over", 125, 200)
        text("Your score is " + str(count),100,300)
        y = 450
        z = 0