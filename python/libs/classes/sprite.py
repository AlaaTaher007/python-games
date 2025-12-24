from os import curdir
from pygame import sprite, transform, image, Surface

class Sprite(sprite.Sprite):
    def __init__(self, _img_path=None, _img_width=150, _img_height=150, _img_col=(150,150, 150)):

        self.img_path = _img_path
        self.img_width = _img_width
        self.img_height = _img_height
        self.img_col = _img_col

        if(_img_path!=None):
            self.image = transform.scale(image.load(curdir + "/" + _img_path), (_img_width, _img_height))
            self.img_width = self.image.get_width()
            self.img_height = self.image.get_height()
        else:
            self.image = Surface((self.img_width, self.img_height))
            self.image.fill(_img_col)