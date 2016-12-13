# drawbot 161212

from sketch_helper import *
from random import uniform

CANVAS = 500
SCALE = 1/2
DIST = 15
DURATION = 1/20

pen = BezierPath()

pen.moveTo((223, 594))
pen.lineTo((410, 594))
pen.curveTo((454, 594), (480, 580), (496, 561))
pen.curveTo((511, 542), (515, 519), (515, 500))
pen.curveTo((515, 428), (478, 402), (399, 402))
pen.lineTo((223, 402))
pen.closePath()
pen.moveTo((223, 0))
pen.lineTo((223, 281))
pen.lineTo((378, 281))
pen.curveTo((434, 281), (463, 272), (479, 250))
pen.curveTo((494, 228), (495, 194), (495, 145))
pen.curveTo((495, 70), (500, 35), (511, 0))
pen.lineTo((677, 0))
pen.lineTo((677, 19))
pen.curveTo((661, 24), (653, 35), (649, 56))
pen.curveTo((645, 76), (645, 110), (645, 162))
pen.curveTo((645, 229), (637, 268), (622, 294))
pen.curveTo((606, 320), (583, 331), (554, 344))
pen.curveTo((626, 368), (665, 435), (665, 515))
pen.curveTo((665, 546), (656, 596), (624, 640))
pen.curveTo((591, 683), (535, 718), (439, 718))
pen.lineTo((76, 718))
pen.lineTo((76, 0))
pen.closePath()

pen.scale(SCALE)

pen_x, pen_y, pen_width, pen_height = pen.bounds()
xMin, yMin, xMax, yMax = pen_x, pen_y, pen_x + pen_width, pen_y + pen_height

yValues = range(int(yMin), int(yMax), DIST)

for n in range(len(y_values)):
    
    newPage(CANVAS, CANVAS)
    
    fill(0.3) 
    rect(0, 0, CANVAS, CANVAS)
    
    translate((CANVAS-pen_width)/2, (CANVAS-pen_height)/2)
    
    fill(0.6)
    drawPath(pen)

    frameDuration(DURATION)
    
    if n == len(y_values)-1:
        frameDuration(DURATION*10)

    for y in range(yValues[0], yValues[n], DIST):
        for x in range(int(xMin), int(xMax), DIST):
            if pen.pointInside((x, y)):
                fill(None)
                strokeWidth(2)
                stroke(1, uniform(0.9, 1), 0)
                rect(x, y, DIST, DIST)

saveSketch("draw")