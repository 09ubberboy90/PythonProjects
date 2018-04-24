import sys, time, math, random
from pyglet.gl import *

window = pyglet.window.Window()
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)
pyglet.resource.path = ['../Resources'] 

class BoundCircle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def distanceSquared(self,other):
        dx = self.center[0] - other.center[0]
        dy = self.center[1] - other.center[1]
        return dx*dx + dy*dy
    def distance(self,other):
        dx = self.center[0] - other.center[0]
        dy = self.center[1] - other.center[1]
        return math.sqrt(dx*dx + dy*dy)
    def containsPoint(self,point):
        dx = self.center[0] - point[0]
        dy = self.center[1] - point[1]
        return dx*dx + dy*dy < self.radius*self.radius
    def collidesCircle(self,other):
        d = self.distanceSquared(other)
        rsum = self.radius + other.radius
        return d <= rsum*rsum
        

class Sprite:
    def __init__(self, width, height, pos, texture):
        self.width = width
        self.height = height
        self.pos = pos
        self.bound = BoundCircle(pos, max(width/2.0,height/2.0))
        if isinstance(texture,pyglet.image.Texture):
            self.texture = texture
        else:
            self.texture = pyglet.image.load(texture).get_texture()
        self.vlist = pyglet.graphics.vertex_list(4, ('v2f',[-width/2.0,-height/2.0,width/2.0,-height/2.0,width/2.0,height/2.0,-width/2.0,height/2.0]), ('t2f', [0,0,1,0,1,1,0,1]))
    def update(self):
        self.bound.center = self.pos
    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], 0)
        if self.texture:
            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture.id)
        glColor3f(1,1,1)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.vlist.draw(GL_QUADS)
        glDisable(GL_BLEND)
        if self.texture:
            glDisable(GL_TEXTURE_2D)
        glPopMatrix()
    def collidesSprite(self,other):
        return self.bound.collidesCircle(other.bound)
        

sprite1 = Sprite(100,75,[400,220],'zelda.jpg')
player = Sprite(50,50,[100,100],'square.jpg')
objects = [ player, sprite1 ]

RED = 1
GREEN = 2
background = GREEN

@window.event
def on_draw():
    global background, objects
    if background == RED:
        glClearColor(1, 0, 0, 0)
    else:
        glClearColor(0.2, 0.3, 0.1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    for o in objects:
        o.draw()


def update(dt):
    global background, objects, player, sprite1

    if keys[pyglet.window.key.UP]:
        player.pos[1] += 5
    elif keys[pyglet.window.key.DOWN]:
        player.pos[1] -= 5
    elif keys[pyglet.window.key.LEFT]:
        player.pos[0] -= 5
    elif keys[pyglet.window.key.RIGHT]:
        player.pos[0] += 5

    for o in objects:
        o.update()

    if player.collidesSprite(sprite1):
        background = RED
    else:
        background = GREEN

pyglet.clock.schedule_interval(update,1/60.0)
pyglet.app.run()