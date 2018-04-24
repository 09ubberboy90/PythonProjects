import pyglet

batch = pyglet.graphics.Batch()


background_level = pyglet.graphics.OrderedGroup(0)
interaction_level = pyglet.graphics.OrderedGroup(1)
enemy_level = pyglet.graphics.OrderedGroup(2)
player_level = pyglet.graphics.OrderedGroup(3)
text_level = pyglet.graphics.OrderedGroup(4)

pyglet.resource.path = ['../Resources'] 
pyglet.resource.reindex()

player_image = pyglet.resource.image("zelda.png")
test_grid = pyglet.image.load("C:/Users/audof/My Documents/LiClipse Workspace/lab/Resources/character.png")
player_seq = pyglet.image.ImageGrid(test_grid,4,4)
player_grid = pyglet.image.TextureGrid(player_seq)
"""anim = pyglet.image.Animation.from_image_sequence(player_grid[(0,0):(0,3)], 2, True)
sprite2 = pyglet.sprite.Sprite(anim)"""
background_image = pyglet.resource.image("back.jpg")
opening_image = pyglet.resource.image("square.jpg")
goblin_image =  pyglet.resource.image("Goblin.png")
spell_image =  pyglet.resource.image("spell.png")
level2_back = pyglet.resource.image("map.png")
player_anim = player_grid.get_animation(1, True)
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()
#window_dimensions = (screen.width, screen.height)

window_dimensions =(1000,850)
def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

center_image(player_image)
center_image(background_image)
center_image(opening_image)
center_image(spell_image)
center_image(goblin_image)
center_image(level2_back)