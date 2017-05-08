# drawbot 170505

from random import uniform, randint
from noise import pnoise1
from sketch_helper import saveSketch

canvas = 500

size(canvas, canvas)

fill(0.9)
rect(0, 0, width(), height())


centx = width()/2
centy = height()/2

stroke(0)
strokeWidth(1.5)

for i in xrange(3):
    
    # stroke(0, random())
    # strokeWidth(uniform(1, 2))
    
    lastx = -999
    lasty = -999
    radius = 90
    radius_noise = uniform(0, 10)

    start_angle = randint(0, 360)
    end_angle = 1440 + randint(0, 1440)
    angle_step = 1 + randint(0, 10)

    for angle in xrange(start_angle, end_angle, angle_step):
        radius += 0.05
        radius_noise += 0.06
        this_radius = radius + (pnoise1(radius_noise) * 50) - 0
        x = centx + cos(radians(angle)) * this_radius
        y = centy + sin(radians(angle)) * this_radius
        if lastx > -999:
            line((lastx, lasty), (x, y))
        lastx = x
        lasty = y

# saveSketch("draw")
        