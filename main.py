from pygame import *
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Platformer")
background = transform.scale(image.load("fon.jpeg"), (win_width, win_height))

#Таймер
clock = time.Clock()
FPS = 60

#Игровой цикл
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0, 0))
    
    display.update()
    clock.tick(FPS)
