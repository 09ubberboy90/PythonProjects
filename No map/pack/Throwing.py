import pyglet

from pack import resources, Enemy
from pack.classes import PhysicalObject


class Spell(PhysicalObject):
    
    def __init__(self, *args, **kwargs):
        super(Spell, self).__init__(img=resources.spell_image, *args, **kwargs)
        self.box = pyglet.sprite.Sprite(img=resources.opening_image, *args, **kwargs)
        self.speed = 20
        self.box.scale = resources.window_dimensions[0] * 4 / 30 / self.box.width
        self.scale = resources.window_dimensions[0] * 4 / 30 / self.width        
        self.box.visible = False
        
        pyglet.clock.schedule_once(self.die, 2)

    def die(self, dt):
        self.dead = True
        self.box.dead = True
        
    def update(self, dt):
        self.x -= self.speed
        self.box.x = self.x
        self.box.y = self.y
    def handle_colision_with(self, other_object):
        if isinstance(other_object, Enemy.Goblin):
            other_object.damaged()
            
            self.dead = True
            print(self.dead)
