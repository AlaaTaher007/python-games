from pygame import *
from os import curdir
#rom random import randint, uniform
from libs.classes.game import Game
from libs.classes.player import Player
from libs.classes.ball import Ball
import time as t
import random
font.init()

game = Game()
game.create_window()

lives = 3

game.set_background("res/backgrounds/bg3.jpg")

player1 = Player(
    _img_path="res/sprites/paddles.png", 
    _img_width=100,
    _img_height=200,
    _img_col=(50, 0, 50), 
    _x=game.win_width - 40,
    _y=game.win_height/2-60
)

player2 = Player(
    _img_path="res/sprites/paddles.png", 
    _img_width=100,
    _img_height=200,
    _img_col=(50, 0, 50), 
    _x=20,
    _y=game.win_height/2-60
)

game.objects.append(player1)
game.objects.append(player2)

balls = []

ball_count = 1

def add_ball():
    ball = Ball("res/sprites/tennis_ball2.png")
    ball.set_width(60)
    ball.set_height(60)

    

    ball.set_x(game.win_width/2)
    ball.set_y(game.win_height/2)
  

    ball.vel_x = random.choice([-3, 3])
    ball.vel_y= random.choice([-2,2])
    balls.append(ball)
    return ball

player_start_position_y = (game.win_height/2) - (player1.img_height/2)

padding = 25
player_start_position_x = game.win_width - player1.img_width - padding

player1.set_x(player_start_position_x)
player1.set_y(player_start_position_y)

player1.set_limit_x(1, game.win_width - player1.img_width)
player1.set_limit_y(1, game.win_height - player1.img_height)


player2.set_x(20)
player2.set_y(player_start_position_y)

player2.set_limit_x(1, game.win_width - player2.img_width)
player2.set_limit_y(1, game.win_height - player2.img_height)

cooldown_start = t.time()

def game_loop():
    global lives
    global ball_count
    
    if(lives<=0):
        print("ded")
        game.running = False

    player1.move_controls(_move_right = False, _move_left = False)
    #player2.move_controls(_move_right = False, _move_left = False)
    if game.is_pressed(K_w):
        player2.set_y(player2.get_pos_y() - 5)
    if game.is_pressed(K_s):
        player2.set_y(player2.get_pos_y() + 5)

    if(len(balls)<=0):
            add_ball()

    for ball in balls:
        ball.set_y(ball.get_pos_y() + ball.vel_y)
        ball.set_x(ball.get_pos_x() + ball.vel_x)

        if(ball.get_pos_y()<= 0 or ball.get_pos_y()>= game.win_height- 40):
            ball.vel_y *= -1
            
        if sprite.collide_rect(ball, player1):
            ball.vel_x =- abs(ball.vel_x) - 0.3

        if sprite.collide_rect(ball, player2):
            ball.vel_x = abs(ball.vel_x) + 0.3
    
        if ball.get_pos_x() < -50 or ball.get_pos_x() > game.win_width + 50:
            balls.remove(ball)
            lives -= 1
            add_ball()

    
        
    #DRAW OBJECTS---------------------------------
    player1.draw(game.window)
    player2.draw(game.window)
    
    for ball in balls:
        ball.draw(game.window)

    #DRAW TEXT
    fontt = font.SysFont("Arial", 30)
    #rendered_font = fontt.render(f"enemies: {len(enemies)}", True, (255, 255, 255))
    #x = game.win_width - rendered_font.get_size()[0]
    #game.window.blit(rendered_font, (x, 0))
    
    game.draw_text(f"lives: {lives}")

    

game.run(game_loop)