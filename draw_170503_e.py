# drawbot 170503

from random import seed
from sketch_helper import saveSketch

canvas = 500
margin = 50
fps = 12
point = 4
frames = 10
dist = 3


for n in xrange(frames):
    newPage(canvas, canvas)
    frameDuration(1/fps)
    
    fill(0)
    rect(0, 0, width(), height())
    
    if n < frames/2:
        n = n
    else:
        n = frames-n

    seed(1)
    for i in xrange(300):
        fill(1)
        oval(margin+random()*(width()-2*margin)+n*dist, margin+random()*(height()-2*margin), point, point)
        fill(1, 0.9)
        oval(margin+random()*(width()-2*margin)+n*dist*0.6, margin+random()*(height()-2*margin), point, point)
        fill(1, 0.6)
        oval(margin+random()*(width()-2*margin)+n*dist*0.3, margin+random()*(height()-2*margin), point, point)
        fill(1, 0.6)
        oval(margin+random()*(width()-2*margin)-n*dist*0.6, margin+random()*(height()-2*margin), point, point)
        fill(1, 0.4)
        oval(margin+random()*(width()-2*margin)-n*dist*0.3, margin+random()*(height()-2*margin), point, point)
        fill(1, 0.3)
        oval(margin+random()*(width()-2*margin)-n*dist, margin+random()*(height()-2*margin), point, point)
        
    
saveSketch("draw")