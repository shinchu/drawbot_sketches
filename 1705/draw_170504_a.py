# drawbot 170504

from sketch_helper import saveSketch

canvas = 500
frames = 30
fps = 24

angle = 0
alpha = 360
step = 4
move = 1

for j in range(frames):

    newPage(canvas, canvas)
    frameDuration(1/fps)
    
    fill(0)
    rect(0, 0, width(), height())
    
    strokeWidth(1)
    lineCap("round")

    centx = width()/2
    centy = height()/2
    radius = 150

    for i in xrange(int(alpha/step)):
        stroke(1, 1, 1, random()*0.2)
        line((centx, centy), (centx + radius * sin(radians(angle+i*step)), centy + radius * cos(radians(angle+i*step))))
        line((centx, centy), (centx - radius * sin(radians(angle+i*step)), centy - radius * cos(radians(angle+i*step))))
        
saveSketch("draw")