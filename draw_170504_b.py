# drawbot 170504

from sketch_helper import saveSketch

canvas = 500
fps = 100

size(canvas, canvas)

fill(1)
rect(0, 0, width(), height())

centx = width()/2
centy = height()/2
radius = 100

stroke(0)
strokeWidth(5)

oval(centx-radius, centy-radius, radius*2, radius*2)

for i in xrange(22):
    newPage(canvas, canvas)
    fill(1)
    rect(0, 0, width(), height())
    frameDuration(1/fps)
    stroke(0)
    strokeWidth(5)
    oval(centx-radius*(1-i/10), centy-radius, radius*2*(1-i/10), radius*2)
    

saveSketch("draw")
