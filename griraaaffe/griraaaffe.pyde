x = 0
increments = 0
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
#giraffe 1
    #head
    fill(255, 240, 69)
    ellipse(x, height/2 - 185, 100, 50)
    #neck
    fill(227, 69, 255)
    ellipse(x-50, height/2 -10, 30, 380)
    #body
    fill(255, 209, 101)
    ellipse(x-100, height/2 + 150, 250, 50)
    fill(255, 107, 107)
    ellipse(x-50, height/2 + 180, 17, 100)
    fill(107, 255, 107)
    ellipse(x-90, height/2 + 180, 17, 100)
    fill(107, 107, 255)
    ellipse(x-130, height/2 + 180, 17, 100)
    fill(255, 181, 107)
    ellipse(x-170, height/2 + 180, 17, 100)
    fill(255, 255, 255)
    ellipse(x+20, height/2 - 190, 30, 30)
    ellipse(x-5, height/2 - 190, 30, 30)
    fill(1, 3, 3)
    ellipse(x +25, height/2 - 195, 10, 10)
    ellipse(x , height/2 - 195, 10, 10)
    ellipse(x + 12, height/2 - 170, 13, 13)
    fill(255, 17, 13)
    ellipse(x+13, height/2 - 167, 9, 9)
    fill(255, 240, 69)
    ellipse(x - 30, height/2 - 213, 27, 42)
#giraffe 2 x-200, height/2-100
    fill(255, 240, 69)
    ellipse(x - 300, height/2 - 285, 100, 50)
    fill(227, 69, 255)
    ellipse(x-350, height/2 -110, 30, 380)
    fill(255, 209, 101)
    ellipse(x-400, height/2 +50, 250, 50)
    fill(255, 107, 107)
    ellipse(x-350, height/2 +80, 17, 100)
    fill(107, 255, 107)
    ellipse(x-390, height/2 +80, 17, 100)
    fill(107, 107, 255)
    ellipse(x-430, height/2 +80, 17, 100)
    fill(255, 181, 107)
    ellipse(x-470, height/2 +80, 17, 100)
    fill(255, 255, 255)
    ellipse(x-280, height/2 - 290, 30, 30)
    ellipse(x-305, height/2 - 290, 30, 30)
    fill(1, 3, 3)
    ellipse(x -275, height/2 - 295, 10, 10)
    ellipse(x -300, height/2 - 295, 10, 10)
    ellipse(x -288, height/2 - 270, 13, 13)
    fill(255, 17, 13)
    ellipse(x-287, height/2 - 267, 9, 9)
#giraffe 3 x-600
    fill(255, 240, 69)
    ellipse(x-600, height/2 - 185, 100, 50)
    fill(227, 69, 255)
    ellipse(x-650, height/2 -10, 30, 380)
    fill(255, 209, 101)
    ellipse(x-700, height/2 + 150, 250, 50)
    fill(255, 107, 107)
    ellipse(x-650, height/2 + 180, 17, 100)
    fill(107, 255, 107)
    ellipse(x-690, height/2 + 180, 17, 100)
    fill(107, 107, 255)
    ellipse(x-730, height/2 + 180, 17, 100)
    fill(255, 181, 107)
    ellipse(x-770, height/2 + 180, 17, 100)
    fill(255, 255, 255)
    ellipse(x-580, height/2 - 190, 30, 30)
    ellipse(x-595, height/2 - 190, 30, 30)
    fill(1, 3, 3)
    ellipse(x -575, height/2 - 195, 10, 10)
    ellipse(x -600, height/2 - 195, 10, 10)
    ellipse(x -588, height/2 - 170, 13, 13)
    fill(255, 17, 13)
    ellipse(x-587, height/2 - 167, 9, 9)
#giraffe 4 x-300, height/2-100
    fill(255, 240, 69)
    ellipse(x - 300, height/2 - 285, 100, 50)
    fill(227, 69, 255)
    ellipse(x-350, height/2 -110, 30, 380)
    fill(255, 209, 101)
    ellipse(x-400, height/2 +50, 250, 50)
    fill(255, 107, 107)
    ellipse(x-350, height/2 +80, 17, 100)
    fill(107, 255, 107)
    ellipse(x-390, height/2 +80, 17, 100)
    fill(107, 107, 255)
    ellipse(x-430, height/2 +80, 17, 100)
    fill(255, 181, 107)
    ellipse(x-470, height/2 +80, 17, 100)
    fill(255, 255, 255)
    ellipse(x-280, height/2 - 290, 30, 30)
    ellipse(x-305, height/2 - 290, 30, 30)
    fill(1, 3, 3)
    ellipse(x -275, height/2 - 295, 10, 10)
    ellipse(x -300, height/2 - 295, 10, 10)
    ellipse(x -288, height/2 - 270, 13, 13)
    fill(255, 17, 13)
    ellipse(x-287, height/2 - 267, 9, 9)

    
    
    if x >= width:
        x = 0
