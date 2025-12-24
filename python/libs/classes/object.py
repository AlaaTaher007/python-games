from os import curdir
from pygame import transform, image, Surface

from libs.classes.sprite import Sprite

class Object(Sprite):

    def __init__(self, _img_path=None, _img_width=150, _img_height=150, _img_col=(255, 255, 255), _x=0, _y=0, _game=None):
        super().__init__(_img_path, _img_width, _img_height, _img_col)
        self.rect = self.image.get_rect()
        self.rect.x = _x
        self.rect.y = _y
        self.speed = 10
        self.limit_left = None
        self.limit_right = None
        self.limit_up = None
        self.limit_down = None
        self.game = _game

    def __del__(self):
        print("object is destroyed")
        if(self.game != None):
            self.game.objects.remove(self)

    def set_x(self, _x):
        self.rect.x = _x

    def set_limit_x(self, _x1, _x2):
        self.limit_left = _x1
        self.limit_right = _x2

    def set_limit_y(self, _y1, _y2):
        self.limit_up = _y1
        self.limit_down = _y2

    def set_y(self, _y):
        self.rect.y = _y

    def set_width(self, _w):
        self.img_width = _w
        self.rect.width = _w

        if(self.img_path!=None):
            self.image = transform.scale(image.load(curdir + "/" + self.img_path), (self.img_width, self.img_height))
        else:
            self.image = Surface((self.img_width, self.img_height))
            self.image.fill(self.img_col)

    def set_height(self, _h):
        self.img_height = _h
        self.rect.height = _h
        if(self.img_path!=None):
            self.image = transform.scale(image.load(curdir + "/" + self.img_path), (self.img_width, self.img_height))
        else:
            self.image = Surface((self.img_width, self.img_height))
            self.image.fill(self.img_col)

    def get_pos_x(self):
            return self.rect.x
        
    def get_pos_y(self):
        return self.rect.y
    
    def get_pos(self):
        return (self.rect.x, self.rect.y)

    def draw(self, _win):
        _win.blit(self.image, (self.rect.x, self.rect.y))

    def move_left(self):
        if (not self.limit_left) or (self.limit_left and self.rect.x>self.limit_left):
            self.rect.x -= self.speed

    def move_right(self):
        if (not self.limit_right) or (self.limit_right and self.rect.x<self.limit_right):
            self.rect.x += self.speed

    def move_up(self):
        if (not self.limit_up) or (self.limit_up and self.rect.y>self.limit_up):
            self.rect.y -= self.speed

    def move_down(self):
        if (not self.limit_down) or (self.limit_down and self.rect.y<self.limit_down):
            self.rect.y += self.speed

