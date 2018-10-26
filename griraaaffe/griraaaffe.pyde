x = 0
increments = 0

def giraffe(x_location, y_location):
    #giraffe 1
    #head
    fill(255, 240, 69)
    rotate(radians(0 + x), )
    ellipse(x_location, y_location - 185, 100, 50)
    #neck
    fill(227, 69, 255)
    ellipse(x_location -50, y_location -10, 30, 380)
    #body
    fill(255, 209, 101)
    ellipse(x_location -100, y_location + 150, 250, 50)
    fill(255, 107, 107)
    ellipse(x_location -50, y_location + 180, 17, 100)
    fill(107, 255, 107)
    ellipse(x_location -90, y_location + 180, 17, 100)
    fill(107, 107, 255)
    ellipse(x_location -130, y_location + 180, 17, 100)
    fill(255, 181, 107)
    ellipse(x_location -170, y_location + 180, 17, 100)
    fill(255, 255, 255)
    ellipse(x_location +20, y_location - 190, 30, 30)
    ellipse(x_location -5, y_location - 190, 30, 30)
    fill(1, 3, 3)
    ellipse(x_location +25, y_location - 195, 10, 10)
    ellipse(x_location , y_location - 195, 10, 10)
    #ellipse(x_location + 12,  - 170, 13, 13)
    fill(255, 17, 13)
    ellipse(x_location +13, y_location - 167, 9, 9)
    fill(255, 240, 69)
    ellipse(x_location - 30, y_location - 213, 27, 42)

def setup():
    size(640, 580)

def draw():
    global x
    global increments
    if x == 0:
        increments = 5
    elif x >= 640:
        increments = -5
    x += increments
    background(20, 251, 255)
    noStroke()
    
    
#backdrop
    fill('#E8FF3B')
    ellipse(x, height/2 -185, 80, 80)
    fill('#1CAA07')
    ellipse(250, 450, 300, 680)
    fill('#21C908')
    ellipse(470, 450, 350, 550)    
    fill('#3CE024')
    ellipse(50, 540, 600, 750)  
    ellipse(640, 480, 300, 740)
    fill(88, 255, 59)
    ellipse(400, 550, 500, 390)
    fill('#73F061')
    rect(0, 500, 740, 100)
#giraffe 1
    #head
    giraffe(200, 300)
    giraffe(400, 300)
    giraffe(600, 300)
    giraffe(800, 300)
    
    
    
    if x >= width:
        x = 0
