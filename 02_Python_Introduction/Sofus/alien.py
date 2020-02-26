import random

alien = Actor('alien')
alien.pos = 100, 56
speed = 6

WIDTH = 1000
HEIGHT = 500

def draw():
    screen.clear()
    alien.draw()

def update():
    global speed
    alien.left += speed
    if alien.left > WIDTH:
        alien.right = 0
        alien.pos = 0, random.randint(50,450)
        speed = random.randint(10,100)
        
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Oof!")
    else:
        print("yeet!")
