from libs.classes.object import Object

class Bullet(Object):
    def __init__(self, 
        _img_path=None, 
        _img_width=50, 
        _img_height=50, 
        _img_col=(255, 255, 255), 
        _x=0, _y=0, 
        _game=None
    ):
        super().__init__(_img_path, _img_width, _img_height, _img_col, _x, _y, _game=_game)
