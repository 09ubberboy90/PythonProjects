from pack import resources, classes, Player
from pack.classes import PhysicalObject
import math
from random import randint
import pyglet

class Goblin(PhysicalObject):
    
    def __init__(self, *args, **kwargs):
        super(Goblin,self).__init__(img=resources.goblin_image, *args, **kwargs)
        self.items = []
        self.hp = 1
        self.box = pyglet.sprite.Sprite(img=resources.opening_image, *args, **kwargs)
        self.x = resources.window_dimensions[0]/5
        self.y = resources.window_dimensions[1]/5
        self.box.scale = resources.window_dimensions[0]*2/20/self.box.width
        self.scale = resources.window_dimensions[0]*2/10/self.width
        classes.flags["Goblin_has_appeared"] = False
        classes.flags["Goblin_dead"] = False

        self.label = classes.Text(*args, **kwargs)
        
        self.box.visible = False
        self.visible = False
        
        self.total_time = 0
        
    def update(self, dt, player):
        self.move_text()
        if classes.flags["Goblin_has_appeared"] == True:
            self.box.x = self.x
            self.box.y = self.y
            self.move_object(dt,player)
            self.visible = True
            self.box.visible = True
            self.move_text()
        else:
            self.visible = False   
    def change_state(self):
        classes.flags["Goblin_has_appeared"] = True 
    def damaged(self):
        self.hp-=randint(30,60)
        if self.hp <= 0:
            classes.flags["Goblin_has_appeared"] = False
            classes.flags["Goblin_dead"] = True
            
    def move_text(self):
        self.label.font_size = 10

        if classes.flags["Goblin_has_appeared"] == True:
            self.label.text = "Hp : %d"%(self.hp)   
            self.label.x = self.x
            self.label.y = self.y+self.height//2+10     
        else:
            self.label.text = ""
            self.label.x = 0
            self.label.y = 0
   
        self.label.newdraw(self.label)
        
    def handle_colision_with(self,other_object):
        if isinstance(other_object, Player.Player):
            other_object.damaged()
            other_object.x = other_object.default_x
            other_object.y = other_object.default_y
            if classes.flags["Level"] == 2:
                dx, dy = self.x - other_object.x, self.y - other_object.y
                dist = math.hypot(dx, dy)
                if dist == 0:
                    dist = 1
                else:
                    dx, dy = dx / dist, dy / dist
                # Throwback!!!!!!!!!!
                self.x += dx * 300
                
                
    def move_object(self,dt,player):
        self.total_time += dt        
        if classes.flags["Level"] == 1:
            self.y += math.sin(self.total_time)/15 * resources.window_dimensions[0]/4
        else:
            dx, dy = self.x - player.x, self.y - player.y
            dist = math.hypot(dx, dy)
            if dist == 0:
                dist = 1
            else:
                dx, dy = dx / dist, dy / dist
    
            self.x -= dx * dt * 150
            self.y -= dy * dt * 150
                