# drawbot 170503

canvas = 500
radius = 10
diam = radius * 2

size(canvas, canvas)

centx = width()/2
centy = height()/2

fill(None)
stroke(0, 50/255)
strokeWidth(1)

fill(20/255, 50/255, 70/255)
stroke(20/255, 50/255, 70/255)

lastx = -999
lasty = -999

radiusNoise = random() * 10

for ang in xrange(0, 1440, 3):
    radiusNoise += 0.05
    radius += 0.1
    thisRadius = radius * radiusNoise
    rad = radians(ang)
    x = centx + (thisRadius * sin(rad))
    y = centy + (thisRadius * cos(rad))
    if lastx > -999:
        line((x, y), (lastx, lasty))
    lastx = x
    lasty = y
 