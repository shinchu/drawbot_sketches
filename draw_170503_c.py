# drawbot 170503

from sketch_helper import *

canvas = 500

size(canvas, canvas)
fill(random(), random(), random(), 0.6)
rect(0, 0, width(), height()/2)
fill(random(), random(), random(), 0.6)
rect(0, height()/2, width(), height()/2)

fill(random(), random(), random(), 0.3)
oval((width()-canvas)/2, (height()-canvas)/2, canvas, canvas)

xstep = 80

for x in xrange(0, width()-xstep, xstep):
    fill(random(), random(), random(), 0.3)
    oval(0, (height()-x)/2, x, x)
    fill(random(), random(), random(), 0.3)
    oval(width()-x, (height()-x)/2, x, x)

savePNG("draw")