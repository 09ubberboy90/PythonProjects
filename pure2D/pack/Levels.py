import pyglet

from pack import resources, classes, Enemy


class Level_Handler(object):
    new_objects = []

    def __init__(self, *args, **kwargs):
        self.levels = {}
        self.actual_level = 0
        self.max_level = 4
    def level_switcher(self, level_to_load):
        self.levels[level_to_load].batch = resources.batch
        self.levels[level_to_load].loader()
        for i in self.levels[level_to_load].level_objects:
            i.batch = resources.batch
    def level_keeper(self, *args, **kwargs):   
        self.levels["1"] = Level_1(*args, **kwargs)
        self.levels["2"] = Level_2(*args, **kwargs)
        self.levels["3"] = Level_3(*args, **kwargs)
        self.levels["4"] = FinalScreen(*args, **kwargs)
        self.actual_level += 1
        if self.actual_level > 0 and self.actual_level <= self.max_level:
            self.level_switcher(str(self.actual_level))
        classes.flags["Level"] = self.actual_level   
         
class Level_1(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        self.level_objects = []
        super(Level_1, self).__init__(img=resources.background_image, group=resources.background_level, *args, **kwargs)
        Level_Handler.__init__(self)
        """
        self.scale = resources.window_dimensions[0] / self.width
        self.x = resources.window_dimensions[0] / 2
        self.y = resources.window_dimensions[1] / 2
        self.goblin = Enemy.Goblin(group=resources.enemy_level)
        #self.square = classes.Interaction(group=resources.interaction_level)
        self.level_objects.append(self.goblin)
        self.level_objects.append(self.square)
        """     
        self.x = 0
        self.y = 0
        self.level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                    PPPPPPPPPPP           P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P    PPPPPPPP                              P",
        "P                                          P",
        "P                          PPPPPPP         P",
        "P                 PPPPPP                   P",
        "P                                          P",
        "P         PPPPPPP                          P",
        "P                                          P",
        "P                     PPPPPP               P",
        "P                                          P",
        "P   PPPPPPPPPPP                            P",
        "P                                          P",
        "P                 PPPPPPPPPPP              P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
        
        self.total_level_width  = len(self.level[0])*32
        self.total_level_height = len(self.level)*32
        for row in self.level:
            for col in row:
                if col == "P":
                    p = classes.Platform(self.x, self.y)
                    self.level_objects.append(p)
                if col == "E":
                    e = classes.ExitBlock(self.x, self.y)
                    self.level_objects.append(e)
                self.x += 32
            self.y += 32
            self.x = 0
    def loader(self):    
        Level_Handler.new_objects.extend(self.level_objects)
    
class Level_2(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        self.level_objects = []
        super(Level_2, self).__init__(img=resources.level2_back, group=resources.background_level, *args, **kwargs)
        Level_Handler.__init__(self)
        self.scale = resources.window_dimensions[0] / self.width
        self.x = resources.window_dimensions[0] / 2
        self.y = resources.window_dimensions[1] / 2
        self.goblin = Enemy.Goblin(group=resources.enemy_level)
        self.square = classes.Interaction(group=resources.interaction_level)
        self.level_objects.append(self.goblin)
        self.level_objects.append(self.square) 
        
    def loader(self):
           
        Level_Handler.new_objects = self.level_objects
        
class Level_3(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        self.level_objects = []
        super(Level_3, self).__init__(img=resources.background_image, group=resources.background_level, *args, **kwargs)
        Level_Handler.__init__(self)
        self.scale = resources.window_dimensions[0] / self.width
        self.x = resources.window_dimensions[0] / 2
        self.y = resources.window_dimensions[1] / 2
        self.goblin = Enemy.Goblin(group=resources.enemy_level)
        self.square = classes.Interaction(group=resources.interaction_level)
        self.level_objects.append(self.goblin)
        self.level_objects.append(self.square) 
        
    def loader(self):
           
        Level_Handler.new_objects = self.level_objects
class FinalScreen(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        self.level_objects = []
        super(FinalScreen, self).__init__(img=resources.opening_image, group=resources.background_level, *args, **kwargs)
        Level_Handler.__init__(self)
        self.scale = resources.window_dimensions[0] / self.width
        self.x = resources.window_dimensions[0] / 2
        self.y = resources.window_dimensions[1] / 2
        self.label = classes.Text(group=resources.text_level) 
        
        
    def loader(self):
        print("called")
        self.label.x = resources.window_dimensions[0] / 2
        self.label.font_size = 36
        self.label.y = resources.window_dimensions[1] / 2
        self.label.text = "You Won !!!"
        self.label.newdraw(self.label)   
        Level_Handler.new_objects = self.level_objects
