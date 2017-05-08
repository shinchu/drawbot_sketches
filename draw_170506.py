# drawbot 170506

from sketch_helper import saveSketch

canvas = 500
fps = 24
frames = 10

radius = 100
step = 3

lastx = -999
lasty = -999

for frame in range(frames):

    newPage(canvas, canvas)
    fill(1)
    rect(0, 0, width(), height())
    
    frameDuration(1/fps)

    centx = width()/2
    centy = width()/2

    start_angle = frame * 10
    end_angle = start_angle + 361

    for angle in range(start_angle, end_angle, step):

        x = centx + sin(radians(angle)) * radius
        y = centy + cos(radians(angle)) * radius
        alpha = angle / (end_angle - start_angle)
    
        if lastx > -999:
            stroke(0, alpha)
            line((x, y), (lastx, lasty))
    
        lastx = x
        lasty = y
    
saveSketch("draw")