def setup():
    size(500,500)
    background(0,0,0)
    fill(255,255,255)
    rect(206,270,100,50,10)
    fill(0,255,0)
    textSize(26)
    text("Welcome to Space Invaders", 100,200)
    textSize(13)
    fill(0,255,0)
    text("Click to Begin", 215,300)
if mousePressed and mouseX < 256 and mouseY < 280 and mouseX > 206 and mouseY > 270:
    background(0,0,0)