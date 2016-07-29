from random import *
def setup():
    size(150,150)
    grid(150,150,30,30)

def grid(width, height, XScale, YScale):
   background(255, 255, 255)
   x = 0
   while x < width:
       line(0, x + YScale, width, x + YScale)
       x += YScale
   x = 0
   while x < height:
       line(x + XScale, 0, x + XScale, height) 
       x += XScale
turns = 0
shots = True
def draw():
    global turns
    if turns < 20:
        if mouseX <= 30 and mouseY <= 30 and mouseX >= 0 and mouseY >= 0:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(0,0,30,30)
                turns = turns + 1
                
        if mouseX <= 30 and mouseY <= 60 and mouseX >= 0 and mouseY >= 30:
            if mousePressed and mouseButton == LEFT:
                fill(0,0,0) 
                rect(0,30,30,30)   
                fill(255,255,255)  
                text("HIT!", 0, 30)        
        if mouseX <= 30 and mouseY <= 90 and mouseX >= 0 and mouseY >= 60:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(0,60,30,30) 
                turns = turns + 1           
        if mouseX <= 30 and mouseY <= 120 and mouseX >= 0 and mouseY >= 90:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(0,90,30,30) 
                turns = turns + 1    
        if mouseX <= 30 and mouseY <= 150 and mouseX >= 0 and mouseY >= 120:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(0,120,30,30)
                turns = turns + 1
        if mouseX <= 60 and mouseY <= 30 and mouseX >= 30 and mouseY >= 0:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(30,0,30,30)
                turns = turns + 1
        if mouseX <= 90 and mouseY <= 30 and mouseX >= 60 and mouseY >= 0:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(60,0,30,30) 
                turns = turns + 1           
        if mouseX <= 120 and mouseY <= 30 and mouseX >= 90 and mouseY >= 0:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(90,0,30,30) 
                turns = turns + 1           
        if mouseX <= 150 and mouseY <= 30 and mouseX >= 120 and mouseY >= 0:
            if mousePressed and mouseButton == LEFT:
                fill(0,0,0) 
                rect(120,0,30,30)    
                fill(255,255,255)  
                text("HIT!", 120, 0)
        if mouseX <= 60 and mouseY <= 60 and mouseX >= 30 and mouseY >= 30:
            if mousePressed and mouseButton == LEFT:
                fill(0,0,0) 
                rect(30,30,30,30)
                fill(255,255,255)  
                text("HIT!", 30, 30)
        if mouseX < 90 and mouseY < 60 and mouseX > 60 and mouseY > 30:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(60,30,30,30)
                turns = turns + 1            
        if mouseX < 120 and mouseY <= 60 and mouseX > 90 and mouseY > 30:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(90,30,30,30)
                turns = turns + 1            
        if mouseX < 150 and mouseY < 60 and mouseX > 120 and mouseY > 30:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(120,30,30,30)
                turns = turns + 1  
        if mouseX < 60 and mouseY < 90 and mouseX > 30 and mouseY > 60:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(30,60,30,30)
                turns = turns + 1
        if mouseX < 90 and mouseY < 90 and mouseX > 60 and mouseY > 60:
            if mousePressed and mouseButton == LEFT:
                fill(0,0,0) 
                rect(60,60,30,30)  
                fill(255,255,255)  
                text("HIT!", 60, 60)        
        if mouseX < 120 and mouseY < 90 and mouseX > 90 and mouseY > 60:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(90,60,30,30)
                turns = turns + 1            
        if mouseX < 150 and mouseY < 90 and mouseX > 120 and mouseY > 60:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(120,60,30,30)
                turns = turns + 1
        if mouseX < 60 and mouseY < 120 and mouseX > 30 and mouseY > 90:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(30,90,30,30)
                turns = turns + 1
        if mouseX < 90 and mouseY < 120 and mouseX > 60 and mouseY > 90:
            if mousePressed and mouseButton == LEFT:
                fill(0,0,0) 
                rect(60,90,30,30)
                fill(255,255,255)  
                text("HIT!", 60, 90)          
        if mouseX < 120 and mouseY < 120 and mouseX > 90 and mouseY > 90:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(90,90,30,30)
                turns = turns + 1            
        if mouseX < 150 and mouseY < 120 and mouseX > 120 and mouseY > 90:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(120,90,30,30)
                turns = turns + 1
        if mouseX < 60 and mouseY < 150 and mouseX > 30 and mouseY > 120:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(30,120,30,30)
                turns = turns + 1
        if mouseX < 90 and mouseY < 150 and mouseX > 60 and mouseY > 120:
            if mousePressed and mouseButton == LEFT:
                fill(0,0,0) 
                rect(60,120,30,30)       
                fill(255,255,255)  
                text("HIT!", 60, 120)    
        if mouseX < 120 and mouseY < 150 and mouseX > 90 and mouseY > 120:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(90,120,30,30) 
                turns = turns + 1           
        if mouseX < 150 and mouseY < 150 and mouseX > 120 and mouseY > 120:
            if mousePressed and mouseButton == LEFT:
                fill(255,0,0) 
                rect(120,120,30,30)
                turns = turns + 1
        if turns == 20:
            fill(0,0,255)
            #font = loadFont("BritannicBold-48.vlw")
            #textFont(font, 75)
            text("Gameover",75,75)                                          