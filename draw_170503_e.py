# drawbot 170503

from random import seed
from sketch_helper import saveSketch

canvas = 500
margin = 30
fps = 24
point = 4
frames = 20
dist = 1.5


for n in xrange(frames):
    newPage(canvas, canvas)
    frameDuration(1/fps)
    
    fill(0)
    rect(0, 0, width(), height())
    
    if n < frames/2:
        n = n
    else:
        n = frames-n

    alpha = 2*n/frames
    seed(1)
    for i in xrange(350):
        fill(1)
        oval(margin+random()*(width()-2*margin)+n*dist-point/2, margin+random()*(height()-2*margin)-point/2, point, point)
        fill(1, 0.9)
        oval(margin+random()*(width()-2*margin)+n*dist*0.6-point/2, margin+random()*(height()-2*margin)-point/2, point, point)
        fill(1, 0.6)
        oval(margin+random()*(width()-2*margin)-point/2, margin+random()*(height()-2*margin)-point/2, point, point)
        fill(1, 0.6)
        oval(margin+random()*(width()-2*margin)-n*dist*0.6-point/2, margin+random()*(height()-2*margin)-point/2, point, point) 
        fill(1, 0.3*alpha)
        oval(margin+random()*(width()-2*margin)-n*dist-point/2, margin+random()*(height()-2*margin)-point/2, point, point)
         
saveSketch("draw")