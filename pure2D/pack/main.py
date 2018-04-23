from pyglet import clock
import pyglet

from pack import classes, resources, Player, Enemy, Throwing, Levels,Camera


entry = resources.batch


background_level = resources.background_level
interaction_level = resources.interaction_level
player_level = resources.player_level
enemy_level = resources.enemy_level
text_level = resources.text_level



class World(pyglet.window.Window):
    
    def __init__(self):
        pyglet.window.Window.__init__(self, resources.window_dimensions[0], resources.window_dimensions[1])
        self.to_delete = []
        self.scoring = 0
        self.attack_label = False
        self.fps_display = clock.ClockDisplay()
        self.level = Levels.Level_Handler(group=background_level)
        self.player = Player.Player(batch=entry, group=player_level)
        self.game_objects = []
        self.game_objects.append(self.player)
        #self.camera = Camera(complex_camera, total_level_width, total_level_height)
        self.level.level_keeper()
        self.schedule = pyglet.clock.schedule_interval(func=self.update, interval=1 / 60.) 
        self.push_handlers(self.player.keyboard)
        self.reappender()
    def update(self, dt):
        for obj_1 in self.game_objects:
            for obj_2 in self.game_objects:
                if not obj_1.dead and not obj_2.dead:
                    if obj_2 is self.player:
                        if self.player.collides_with(obj_1.box):
                            if isinstance(obj_1, classes.Interaction) :  # Player collisionbox
                                self.player.handle_colision_with(obj_1)
                                obj_1.dead = True
                                self.attack_label = True
                                Enemy.Goblin.change_state(Enemy.Goblin)
                            if isinstance(obj_1, Enemy.Goblin) and self.attack_label:
                                self.player.handle_colision_with(obj_1)
                                obj_1.handle_colision_with(self.player)
                                if obj_1.hp <= 0:
                                    obj_1.dead = True
                                    self.level.level_keeper()
                                    self.reappender()
                                if self.player.hp <= 0:
                                    obj_2.dead = True
                            if isinstance(obj_1, classes.Platform):
                                self.sideHandler(obj_1)
                    elif isinstance(obj_2, Throwing.Spell):  # Spell collisionbox
                        if obj_2.collides_with(obj_1.box):
                            if isinstance(obj_1, Enemy.Goblin) and self.attack_label :
                                obj_2.handle_colision_with(obj_1)
                                if obj_1.hp <= 0:
                                    obj_1.dead = True
                                    self.level.level_keeper()
                                    self.reappender()
                            
                            
        for obj in self.game_objects:
            if isinstance(obj, Enemy.Goblin):
                obj.update(dt, self.player)
            else : 
                obj.update(dt)
            self.game_objects.extend(obj.new_objects)
            obj.new_objects = []
        ids_to_remove = [obj for obj in self.game_objects if obj.dead]
        for id_to_remove in ids_to_remove:
            self.game_objects.remove(id_to_remove)
            id_to_remove.delete()
    def on_draw(self):
        World.clear(self)
        entry.draw()
        self.fps_display.draw()
    def reappender(self):   
        self.game_objects.extend(self.level.new_objects)
    def sideHandler(self,obj):
        if self.player.x < obj.x+obj.width/2:
            self.player.x = obj.x+obj.width/2
            self.player.y = obj.y
        elif self.player.x > obj.x+obj.width/2:
            self.player.x = obj.x+self.player.width
            self.player.y = obj.y
        elif self.player.y < obj.y+obj.height/2:
            self.player.y = obj.y+obj.height
            self.player.x = obj.x
        elif self.player.y > obj.y+obj.height/2 :
            self.player.x= obj.x
            self.player.y = obj.y-self.player.height
app = World()
pyglet.app.run()
