from random import randint

import pyglet
from pyglet.window import key

from pack import resources, classes, Enemy, Throwing
from pack.classes import PhysicalObject


player_pos = (0, 0)
class Player(PhysicalObject):
    
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)
        self.keys = []  
        self.box = pyglet.sprite.Sprite(img=resources.opening_image, *args, **kwargs)
        self.hp = 100
        self.x = resources.window_dimensions[0] * 4 / 5
        self.y = resources.window_dimensions[1] / 4       
        self.default_x = self.x
        self.default_y = self.y
        
        self.keyboard = key.KeyStateHandler()
        self.box.visible = False
        self.box.scale = resources.window_dimensions[0] / 10 / self.box.width
        self.scale = resources.window_dimensions[0] / 10 / self.width
        self.label = classes.Text(*args, **kwargs)
        self.score = classes.Text(*args, **kwargs)
        self.score_value = 0
        
    def move_text(self):
        self.label.text = "Hp : %d" % (self.hp)        
        self.label.x = self.x
        self.label.y = self.y + self.height // 2 + 10 
        self.label.font_size = 10
        self.label.newdraw(self.label)
        
    def score_handler(self):   
        self.score.text = "Score : %d" % (self.score_value)        
        self.score.x = resources.window_dimensions[0] * 2 / 15
        self.score.y = resources.window_dimensions[1] * 14 / 15
        self.score.font_size = 15
        self.score.newdraw(self.score)

    def update(self, dt):
        
        PhysicalObject.update(PhysicalObject)
        #self.check_bounds()
        if self.keyboard[key.LEFT]:
            self.x -= 500 * dt
        elif self.keyboard[key.RIGHT]:
            self.x += 500 * dt
        if self.keyboard[key.UP]:
            self.y += 500 * dt
        elif self.keyboard[key.DOWN]:
            self.y -= 500 * dt
            
        if self.keyboard[key.SPACE] and classes.flags["Spell_loaded"]:
            self.fire()
            classes.flags["Spell_loaded"] = False
            pyglet.clock.schedule_once(self.reload_spell, 1)
            
        if classes.flags["Goblin_dead"]:
                self.score_increase()
                classes.flags["Goblin_dead"] = False
        self.move_text()
        self.score_handler()
        self.box.x = self.x
        self.box.y = self.y
        if classes.flags["Player_dead"]:
            self.death()
        player_pos = (self.x, self.y)   
    def score_increase(self):  
        self.score_value += randint(75, 150)
        print("called")
    def death(self):
            self.label.text = "GAME OVER!!!"
            self.label.x = resources.window_dimensions[0] / 2
            self.label.y = resources.window_dimensions[1] / 2
            self.label.font_size = 50
            self.label.newdraw(self.label)
        
            self.score_value = -9999
            self.score_handler()
            
    def reload_spell(self, dt):    
        classes.flags["Spell_loaded"] = True
        
    def handle_colision_with(self, other_object):
        if isinstance(other_object, classes.Interaction):
            self.x = self.default_x
            self.y = self.default_y
        if isinstance(other_object, Enemy.Goblin):
            other_object.damaged()
            self.x = self.default_x
            self.y = self.default_y
            
    def fire(self):
        spell = Throwing.Spell(x=self.x - self.width // 2 + 10, y=self.y, batch=self.entry)
        spell.visible = True
        self.new_objects.append(spell)
        
    def damaged(self):
        self.hp -= randint(0, 10)
        if self.hp <= 0:
            classes.flags["Player_dead"] = True
