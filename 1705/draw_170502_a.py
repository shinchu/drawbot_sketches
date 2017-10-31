# drawbot 170502

for i in xrange(10):

    newPage(500, 500)
    
    fps = 12

    step = 10
    lastx = -999
    lasty = -999
    y = 50

    borderx = 20
    bordery = 10
    
    frameDuration(1/fps)
    
    strokeWidth(3)
    stroke(0)
    
    for x in xrange(borderx, width()-borderx, step):
        y = bordery + random() * (height() - 2*bordery)
        if lastx > -999:
            line((x, y), (lastx, lasty));
        lastx = x
        lasty = y
    
