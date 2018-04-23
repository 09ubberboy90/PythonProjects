import pyglet 
from pack import resources
import math from pyglet.window
from pyglet.window import key

class player():
    
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.player_image, *args, **kwargs)
        self.keys = []  
        self.box = pyglet.sprite.Sprite(img=resources.opening_image, *args, **kwargs)
        self.box.visible = False

    def on_key_press(self, symbol, modifiers):
        self.keys.append(symbol)
        if symbol == key.A:
            print( 'The "A" key was pressed.')
        elif symbol == key.ESCAPE:
            quit()

            
    def on_key_release(self, symbol, modifiers):
        self.keys.pop(self.keys.index(symbol))

    def update(self,interval):
        if pyglet.window.key.LEFT in self.keys:
            self.x -= 500*interval
            self.box.x-= 500*interval
        elif pyglet.window.key.RIGHT in self.keys:
            self.x += 500*interval
            self.box.x += 500*interval
        elif pyglet.window.key.UP in self.keys:
            self.y += 500*interval
            self.box.y += 500*interval

        elif pyglet.window.key.DOWN in self.keys:
            self.y -= 500*interval
            self.box.y -= 500*interval

class goblin():
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.goblin_image, *args, **kwargs)
class spell():
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.spell_image, *args, **kwargs)
class interaction():
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.opening_image, *args, **kwargs)       