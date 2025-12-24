from libs.classes.object import Object

class Player(Object):
    def __init__(self, _img_path=None, _img_width=150, _img_height=150, _img_col=(255, 255, 255), _x=0, _y=0):
        super().__init__(_img_path, _img_width, _img_height, _img_col, _x, _y)
        self.cooldown = 0.5
    
    def move_controls(self, _move_left=True, _move_right=True, _move_up=True, _move_down=True):

        from pygame import key, K_LEFT, K_RIGHT, K_UP, K_DOWN
        pressed_keys = key.get_pressed()
        
        if _move_left and pressed_keys[K_LEFT]:
            self.move_left()

        if _move_right and pressed_keys[K_RIGHT]:
            self.move_right()

        if _move_up and pressed_keys[K_UP]:
            self.move_up()

        if _move_down and pressed_keys[K_DOWN]:
            self.move_down()