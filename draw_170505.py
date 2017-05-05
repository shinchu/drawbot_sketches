# drawbot 170505

from random import uniform, randint
from noise import pnoise1
from sketch_helper import saveSketch

canvas = 500

size(canvas, canvas)

fill(1)
rect(0, 0, width(), height())


centx = width()/2
centy = height()/2

stroke(0)
strokeWidth(1)

for i in xrange(20):
    
    # stroke(random(), random(), random(), random())
    # strokeWidth(uniform(0.1, 1))
    
    lastx = -999
    lasty = -999
    radius = 30
    radius_noise = uniform(5, 20)

    start_angle = randint(0, 360)
    end_angle = 1440 + randint(0, 1440)
    angle_step = 10 + randint(0, 5)

    for angle in xrange(start_angle, end_angle, angle_step):
        radius += 0.4
        radius_noise += 0.1
        this_radius = radius + (pnoise1(radius_noise) * 80) - 10
        x = centx + cos(radians(angle)) * this_radius
        y = centy + sin(radians(angle)) * this_radius
        if lastx > -999:
            line((lastx, lasty), (x, y))
        lastx = x
        lasty = y

# saveSketch("draw")
        