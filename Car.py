from random import * 
size(700, 700)   

background(04, 250, 0)
fill(0)
rect(0, 70, 700, 100)
fill(255)
rect(0, 110, 100, 20)
rect(200, 110, 100, 20)
rect(400, 110, 100, 20)
rect(600, 110, 100, 20)

blue = color(0,0,255)
red = color(255, 0, 0)
green = color(0,255,0)
black = color(0,0,0)
white = color(255, 255, 255)
random = randint(0, 256)
def make_car(stripe, name, body, tire, textcolor):
    if body == blue:
        fill(0,0,255)
    elif body == red:
        fill(255,0,0)
    elif body == green:
        fill(0,255,0)        
    elif body == black:
        fill(0,0,0)
    elif body == white:
        fill(255,255,255)
    else:
        fill(random)
    noStroke()      
    rect(190, 100, 200, 50)
    triangle(390,100,390,150,440,125)
    if stripe == blue:
        fill(0,0,255)
    elif stripe == red:
        fill(255,0,0)
    elif stripe == green:
        fill(0,255,0)        
    elif stripe == black:
        fill(0,0,0)
    elif stripe == white:
        fill(255,255,255)
    else:
        fill(random)    
    rect(215,135,150,15)
    rect(215,100,150,15)
    if  tire == blue:
        fill(0,0,255)
    elif tire == red:
        fill(255,0,0)
    elif tire == green:
        fill(0,255,0)        
    elif tire == black:
        fill(0,0,0)
    elif tire == white:
        fill(255,255,255)
    else:
        fill(random)    
    ellipse(190, 90, 30, 15)      
    ellipse(190, 160, 30, 15)      
    ellipse(390, 90, 30, 15)      
    ellipse(390, 160, 25, 15)
    fill(255,255,255)
    if textcolor == blue:
        fill(0,0,255)
    elif textcolor == red:
        fill(255,0,0)
    elif textcolor == green:
        fill(0,255,0)        
    elif textcolor == black:
        fill(0,0,0)
    elif textcolor == white:
        fill(255,255,255)
    else:
        fill(random)
    textSize(15)
    text(name, 250, 130)
    
make_car(red, "Speed Racer", random, blue, green)