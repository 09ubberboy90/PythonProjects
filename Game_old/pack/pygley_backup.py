from pyglet import *
from pyglet.window import key
import pyglet

main_batch = pyglet.graphics.Batch()
entry= pyglet.graphics.Batch()
dungeon = pyglet.graphics.Batch()

door_label = True
monster_label = True

background_level = pyglet.graphics.OrderedGroup(0)
interaction_level = pyglet.graphics.OrderedGroup(1)
player_level = pyglet.graphics.OrderedGroup(2)
text_level = pyglet.graphics.OrderedGroup(3)

pyglet.resource.path = ['../Resources'] 

Player_image = pyglet.resource.image("zelda.png")
background_image = pyglet.resource.image("back.jpg")
opening_image = pyglet.resource.image("square.jpg")
goblin_image =  pyglet.resource.image("Goblin.png")

background = pyglet.sprite.Sprite(img = background_image, x=0, y=0, batch=entry, group=background_level)
player = pyglet.sprite.Sprite(img=Player_image, x=400, y=250,batch=entry, group=player_level)
square = pyglet.sprite.Sprite(img=opening_image, x=335, y=435,batch=entry, group=interaction_level)
goblin_square = pyglet.sprite.Sprite(img=opening_image, x=0, y=0,batch=entry, group=interaction_level)
goblin = pyglet.sprite.Sprite(img=goblin_image, x=0, y=0,batch=entry, group=player_level)
player_square = pyglet.sprite.Sprite(img=opening_image, x=400, y=250,batch=entry, group=interaction_level)
monster_hp = pyglet.text.Label(text="Hp: 100", x=20, y=200,batch=entry, group=text_level)

score_label = pyglet.text.Label(text="Hp: 100", x=10, y=575,batch=entry, group=text_level)
player.scale = 0.2
goblin.scale = 0.1
goblin_square.scale = 0.8
player_square.scale = 0.5
player_square.opacity = 0
square.opacity = 0
goblin.opacity = 0
goblin_square.opacity = 0

monster_hp.color = (0,0,0,0)
pyglet.resource.reindex()


class Game(pyglet.window.Window):
    
    def __init__(self):
        pyglet.window.Window.__init__(self,800, 750)
        self.keys = []
        self.schedule = pyglet.clock.schedule_interval(func = self.update, interval = 1/60.) 
        self.scoring = 0
        self.monster_hp_value = 100
    def on_key_press(self,symbol, modifiers):
        self.keys.append(symbol)
        if symbol == key.A:
            print( 'The "A" key was pressed.')
        elif symbol == key.ESCAPE:
            quit()

            
    def on_key_release(self,symbol, modifiers):
        self.keys.pop(self.keys.index(symbol))
    
    def update(self,interval):
        if pyglet.window.key.LEFT in self.keys:
            player.x -= 500*interval
            player_square.x -= 500*interval
        elif pyglet.window.key.RIGHT in self.keys:
            player.x += 500*interval
            player_square.x += 500*interval
        elif pyglet.window.key.UP in self.keys:
            player.y += 500*interval
            player_square.y += 500*interval

        elif pyglet.window.key.DOWN in self.keys:
            player.y -= 500*interval
            player_square.y -= 500*interval

    def on_draw(self):
        Game.clear(self)
        main_batch.draw()
        entry.draw()

        self.outside_border()
        if door_label:
            self.pos(square,"door")
        elif monster_label:
            self.pos(goblin_square,"goblin")
            

    def outside_border(self):
        if player.x <0:
            player.x = self.width
            player_square.x = self.width

        elif player.x > self.width:
            player.x = 0
            player_square.x = 0

        elif player.y <0:
            player.y = self.height
            player_square.y = self.height

        elif player.y > self.height:
            player.y = 0
            player_square.y = 0
            
    def pos(self,object,goal):
        global door_label,monster_label
        #and player.x + player.width> object.x and player.x+ player.width <object.x+object.width and player.y + player.height> object.y and player.y+ player.height <object.y+object.height
        if player_square.x > object.x and player_square.x <object.x+object.width and player_square.y > object.y and player_square.y <object.y+object.height and player_square.x + player_square.width> object.x and player_square.x+ player_square.width <object.x+object.width and player_square.y + player_square.height> object.y and player_square.y+ player_square.height <object.y+object.height:
            if goal == "door":
                self.door_interaction()
                door_label = False
            elif goal == "goblin":
                if self.monster_hp_value == 10:
                    monster_label = False
                self.monster_interaction()
                
    def door_interaction(self):
        player.x = 600
        player.y = 200
        player_square.x = 600
        player_square.y = 200
        self.object_place(goblin,300, 200,255)
        self.object_place(goblin_square, 300, 200,0)
        self.text_place(monster_hp, goblin.x, goblin.y+goblin.height+10)
        self.delete(square)
        
    def monster_interaction(self):
        self.monster_hp_value -=10
        monster_hp.text = "Hp = %d"%self.monster_hp_value
        player.x = 600
        player.y = 300
        player_square.x = 600
        player_square.y = 300
        if self.monster_hp_value == 0:
            self.delete(goblin)
            self.delete(monster_hp)
            self.delete(goblin_square)

    def text_place(self,object,pos_x,pos_y):
        object.color = (255,255,255,255)
        object.x = pos_x
        object.y = pos_y

    def object_place(self,object,pos_x,pos_y,opacity):
        object.opacity = opacity
        object.x = pos_x
        object.y = pos_y
        
    def delete(self,objects):
        objects.delete()
     
window = Game()

pyglet.app.run()