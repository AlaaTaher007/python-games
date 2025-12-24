from os import curdir
import os
from pygame import *

from libs.classes.object import Object

class Game():
    def __init__(self):
        super().__init__()
        self.clock = time.Clock()
        self.fps = 60
        self.running = True
        self.pressed_keys = None
        self.win_width = None
        self.win_height = None
        self.win_caption = None
        self.objects = []
        self.game_id = os.getpid()


    def set_background(self, _bg):
        img = image.load(_bg)
        self.window_background = transform.scale(img, (self.win_width, self.win_height))
        return self.window_background

    def create_window(self, _width=800, _height=500, _caption="game"):

        self.win_width = _width
        self.win_height = _height
        self.win_caption = _caption

        self.window = display.set_mode((self.win_width, self.win_height))

        display.set_caption(self.win_caption)

        return self.window
    
    def event_draw(self, _event_func):
        _event_func()

    def handle_events(self):
        for e in event.get():
            if e.type == QUIT:
                self.end_game(K_ESCAPE)
                break

    def play_sound(Self, _sound):
        mixer.init()
        sound = mixer.Sound(curdir + _sound)
        return sound.play()

    def is_pressed(self, _key):
        if self.pressed_keys[_key]:
            return True
        return False
    
    def end_game(self, _key):
        if self.is_pressed(_key):
            self.running = False

    def run(self, _run_func):

        while self.running:

            #GET PRESSED KEYS AT ANY GIVEN MOMENT
            self.pressed_keys = key.get_pressed()

            #DRAW BACKGROUND -- MUST BE DONE BEFORE OTHER SPRITES
            self.window.blit(self.window_background, (0, 0)) 

            #RUN USER FUNCTION
            _run_func()

            #END GAME WITH KEY PRESS
            self.end_game(K_ESCAPE)

            #HANDLE EVENTS
            self.handle_events()

            #FPS
            self.clock.tick(self.fps)

            #UPDATE WINDOW DISPLAY SO THAT YOU CAN SEE OBJECTS MOVE WITHOUT PROBLEMS
            display.update()

    def end(self):
        self.running = False

    def add_object(_text):
        enemy = Object("res/sprites/enemy_ship.png")
        # enemy.speed = 1
        # enemy.set_x(randint(0, game.win_width))
        # enemy.set_width(60)
        # enemy.set_height(60)
        # enemies.append(enemy)
        # return enemy

    def draw_text(self, _text, _size=30, _font="Arial", _color=(255, 255, 255), _x=0, _y=0):
        fontt = font.SysFont(_font, _size)
        rendered_font = fontt.render(_text, True, _color)
        self.window.blit(rendered_font, (_x, _y))