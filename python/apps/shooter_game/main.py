from pygame import *
from os import curdir
from random import randint, uniform
from libs.classes.game import Game
from libs.classes.player import Player
from libs.classes.enemy import Enemy
from libs.classes.bullet import Bullet
import time as t

font.init()

game = Game()
game.create_window()

lives = 3

game.set_background("res/backgrounds/space.png")

player = Player(
    _img_path="res/sprites/player_ship.png", 
    _img_width=50, 
    _img_height=50, 
    _img_col=(50, 0, 50), 
    _x=0, 
    _y=0
)

game.objects.append(player)

bullets = []
enemies = []

enemy_count = 1

def add_enemy():
    enemy = Enemy("res/sprites/enemy_ship.png")
    enemy.speed = uniform(0.5, 1)
    enemy.set_x(randint(0, game.win_width))
    enemy.set_width(60)
    enemy.set_height(60)
    enemies.append(enemy)
    return enemy

player_start_position_x = (game.win_width/2) - (player.img_width/2)

padding = 25
player_start_position_y = game.win_height - player.img_height - padding

player.set_x(player_start_position_x)
player.set_y(player_start_position_y)

player.set_limit_x(1, game.win_width - player.img_width)
player.set_limit_y(1, game.win_height - player.img_height)

cooldown_start = t.time()

def game_loop():

    global enemy_count
    global lives
    global cooldown_start
    
    if(lives<=0):
        print("ded")
        game.running = False

    player.move_controls(_move_up=False, _move_down=False)

    #WHEN WE KILL ALL ENEMIES PRESENT, 
    #ADD ONE MORE ENEMY
    #AND SPAWN THEM BASED ON ENEMY_COUNT
    if(len(enemies)<=0):
        enemy_count += 1
        for i in range(enemy_count):
            add_enemy()
    
    if(game.is_pressed(K_SPACE)):
        if(t.time() - cooldown_start >= player.cooldown):
            cooldown_start = t.time()
            bullet = Bullet("res/sprites/bullet.png", _game=game)
            game.objects.append(bullet)
            bullet.set_x(player.get_pos_x())
            bullet.set_y(player.get_pos_y())
            bullets.append(bullet)
            game.play_sound("/res/sounds/shoot.wav")
            print("number of objects:", len(game.objects))

    for bullet in bullets:
        bullet.set_y(bullet.get_pos_y() - bullet.speed)
        if(bullet.get_pos_y() < 0):
            # bullet.kill()
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.set_y(enemy.get_pos_y() + enemy.speed)

        if(enemy.get_pos_y()>game.win_height):
            enemies.remove(enemy)
            lives -= 1
            add_enemy()

    for enemy in enemies:
        for bullet in bullets:
            touch = sprite.collide_rect(enemy, bullet)
            if(touch):
                enemies.remove(enemy)
                bullets.remove(bullet)
                game.play_sound("/res/sounds/destroyed.wav")

                # add_enemy()
    #DRAW OBJECTS---------------------------------
    player.draw(game.window)
    
    for enemy in enemies:
        enemy.draw(game.window)

    for bullet in bullets:
        bullet.draw(game.window)

    #DRAW TEXT
    fontt = font.SysFont("Arial", 30)
    rendered_font = fontt.render(f"enemies: {len(enemies)}", True, (255, 255, 255))
    x = game.win_width - rendered_font.get_size()[0]
    game.window.blit(rendered_font, (x, 0))
    
    game.draw_text(f"lives: {lives}")

    

game.run(game_loop)