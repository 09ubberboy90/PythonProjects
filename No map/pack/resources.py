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

background_image = pyglet.resource.image("back.jpg")
opening_image = pyglet.resource.image("square.jpg")
goblin_image = pyglet.resource.image("Goblin.png")
spell_image = pyglet.resource.image("spell.png")
level2_back = pyglet.resource.image("map.png")

platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_default_screen()
window_dimensions = (1000, 850)

#opening_image.blit_to_texture(background_image, window_dimensions[1] / 2, window_dimensions[1] * 2 / 3,0)
# window_dimensions = (screen.width, screen.height)


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

center_image(player_image)
center_image(background_image)
center_image(opening_image)
center_image(spell_image)
center_image(goblin_image)
center_image(level2_back)
