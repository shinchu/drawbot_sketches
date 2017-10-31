# drawbot 170503

size(500, 100)

fill(255/255)
rect(0, 0, width(), height())

stroke(0, 30/255)
line((20, 50), (480, 50))

stroke(20/255, 50/255, 70/255)

xstep = 1
lastx = -999
lasty = -999
angle = 0
y = 50

for x in xrange(20, 480, xstep):
    rad = radians(angle)
    y = 50 + (pow(sin(rad), 3) * 30)
    if lastx > -999:
        line((x, y), (lastx, lasty))
    lastx = x
    lasty = y
    angle += 1