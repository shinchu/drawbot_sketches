# drawbot 170503

from sketch_helper import *

canvas = 500
margin = 0
step = 10

size(canvas, canvas)

for i in xrange(margin, canvas-margin, step):
    for j in xrange(margin, canvas-margin, step):
        fill(j/(canvas-margin), i/(canvas-margin), 0.7, 1)
        rect(i, j*random()+margin, step, step)
        rect(i*random()+margin, height()-margin-(j*random()), step, step)
        
# savePNG("draw")