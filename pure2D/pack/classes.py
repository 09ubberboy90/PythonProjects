from collections import OrderedDict

import pyglet 

from pack import resources
from pack.util import distance


flags = OrderedDict()
flags["Goblin_has_appeared"] = False
flags["Spell_loaded"] = True
flags["Goblin_dead"] = False
flags["Player_dead"] = False
flags["Up_Limit"] = False
flags["Level"] = 0
class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        self.entry = resources.batch
        self.dead = False
        self.new_objects = []
        self.collinding = False

    def update(self):
        pass
    def check_bounds(self):
        min_x = 0
        min_y = 0
        max_x = resources.window_dimensions[0]
        max_y = resources.window_dimensions[1]
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
            
    def collides_with(self, other_object):
        collision_distance = self.image.width / 2 * self.scale + other_object.image.width / 2 * self.scale
        actual_distance = distance(self.position, other_object.position)
        return (actual_distance <= collision_distance)

    def handle_collision_with(self, other_object):
        if other_object.__class__ == self.__class__:
            self.dead = False
            
class Text(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        self.label = pyglet.text.Label("", anchor_x='center', anchor_y='center', *args, **kwargs)
        self.score = pyglet.text.Label("", anchor_x='center', anchor_y='center', *args, **kwargs)
        
                
    def newdraw(self, new):
        self.label.text = new.text        
        self.label.x = new.x
        self.label.y = new.y
        self.label.font_size = new.font_size
        self.label.batch = resources.batch
        
class Interaction(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Interaction, self).__init__(img=resources.opening_image, *args, **kwargs)
        self.dead = False
        self.x = resources.window_dimensions[0] / 2
        self.y = resources.window_dimensions[1] * 2 / 3
        self.box = pyglet.sprite.Sprite(img=resources.opening_image, *args, **kwargs)
        self.box.x = self.x
        self.box.y = self.y
        self.box.visible = False
        self.visible = True
        
    def update(self, dt):
        PhysicalObject.update(self)
        # TO BE DONE : FIGURE OUT A WAY TO ADJUST THE SCALE
        # self.scale = 175*int(Level_1.scale)/self.width
        # self.box.scale = 175*Level_1._scale/self.width
class Platform(PhysicalObject):
    def __init__(self, x,y,*args, **kwargs):
        super(Platform, self).__init__(img=resources.blocks, *args, **kwargs)
        self.box = pyglet.sprite.Sprite(img=resources.blocks, *args, **kwargs)
        self.x = x
        self.y = y

        self.box.x = self.x
        self.box.y = self.y
        self.dead = False

    def update(self, dt):
        pass

class ExitBlock(Platform):
    def __init__(self, x,y,*args, **kwargs):
        super(Platform, self).__init__(img=resources.blocks, *args, **kwargs)
        self.box = pyglet.sprite.Sprite(img=resources.blocks, *args, **kwargs)
        self.x = x
        self.y = y
        self.box.x = self.x
        self.box.y = self.y
        self.dead = False
    def update(self, dt):
        pass