from tkinter import *

class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        #self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    
    def client_exit(self):
        exit()

class elf:
    def __init__(self):
        self.stre = 20
        self.inte = 80
        self.agi = 80
        self.magic_resistance = 80
        self.resistance = 20
        self.kind = 2
        self.kind_name = "elf"    
    
class human:
    def __init__(self):
        self.stre = 60
        self.inte = 60
        self.agi = 60
        self.magic_resistance = 50
        self.resistance = 50
        self.kind = 1
        self.kind_name = "human"
    
        
class dwarf:
    def __init__(self):
        self.stre = 80
        self.inte = 30
        self.agi = 50
        self.magic_resistance = 20
        self.resistance = 80
        self.kind = 3
        self.kind_name = "dwarf"

class player:
    def __init__(self):
        self.base_health = 300
        self.money = 0
        self.level = 1
        self.health = 300
        self.exp = 0
        self.xp_low = 5
        self.xp_high = 50
        self.money_low = 2
        self.money_high = 20
        self.xp_for_level = 50
    def add_up(self, new):
        self.stre = new.stre*1.2
        self.inte = new.inte*1.2
        self.agi = new.agi*1.2
        self.magic_resistance = new.magic_resistance*1.2
        self.resistance = new.resistance*1.2
        self.kind = new.kind
        self.kind_name = new.kind_name
    def level_up(self):
        self.stre *= 1.2
        self.agi *= 1.2
        self.inte *= 1.2
        self.magic_resistance *= 1.1
        self.resistance *= 1.1
        self.exp -= self.xp_for_level
        self.level +=1
        
class enemy:
    def __init__(self):
        self.base_health = 100
        self.money = 0
        self.level = 1
        self.health = 100
        self.exp = 0
        self.xp_for_level = 50
        self.xp_low = 5
        self.xp_high = 50
    def add_up(self, new):
        self.stre = new.stre
        self.inte = new.inte
        self.agi = new.agi
        self.magic_resistance = new.magic_resistance
        self.resistance = new.resistance
        self.kind = new.kind
        self.kind_name = new.kind_name
    def level_up(self):
        self.stre *= 1.2
        self.agi *= 1.2
        self.inte *= 1.2
        self.magic_resistance *= 1.1
        self.resistance *= 1.1
        self.exp -= self.xp_for_level
        self.level += 1
        