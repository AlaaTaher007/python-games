from pygame import *
from os import curdir
from libs.classes.player import Player
from libs.classes.wall import Wall

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
img = image.load("res/backgrounds/bg.jpg")
background = transform.scale(img, (win_width, win_height))
# mixer.init()
# sound = mixer.Sound(curdir + "/res/effect.mp3")
game = True
# sound.play()

player = Player(_img_width=50, _img_height=50, _img_col=(50, 0, 50), _x=0, _y=0)
player.set_x(100)
player.set_y(100)

clock = time.Clock()
while game:

    # player.set_height(player.rect.height + 1)
    # player.set_width(player.rect.width + 1)

    pressed_keys = key.get_pressed()

    if pressed_keys[K_ESCAPE]:
        game = False

    if pressed_keys[K_LEFT]:
        print("Left")
        player.rect.x -= player.speed

    if pressed_keys[K_RIGHT]:
        print("Right")
        player.rect.x += player.speed

    if pressed_keys[K_UP]:
        print("Up")
        player.rect.y -= player.speed

    if pressed_keys[K_DOWN]:
        print("Down")
        player.rect.y += player.speed

    for e in event.get():
        if e.type == QUIT:
            game = False
            break
    
    window.blit(background, (0, 0))
    player.draw(window)
    clock.tick(60)
    display.update()
