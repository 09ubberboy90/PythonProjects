import pyglet 
from pack import resources,util
from pyglet.window import key


class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        self.dead = False
        self.new_objects = []

    def collides_with(self, other_object):
        collision_distance = self.image.width/2*self.scale + other_object.image.width/2*self.scale
        actual_distance = util.distance( self.position, other_object.position)
        return (actual_distance <= collision_distance)

    def handle_collision_with(self, other_object):
        if other_object.__class__ == self.__class__:
            self.dead = False
        else:
            self.dead = True

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        self.check_bounds()

    def check_bounds(self):
        min_x = 0
        min_y = -0
        max_x = 800
        max_y = 750
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y

class player(PhysicalObject):
    
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

class goblin(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.goblin_image, *args, **kwargs)
class spell(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.spell_image, *args, **kwargs)
class interaction():
    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.opening_image, *args, **kwargs)       