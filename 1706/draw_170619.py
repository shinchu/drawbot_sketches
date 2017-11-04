# drawbot 161115

from sketch_helper import *

def drawHandle(path, r):

    for contour in path:
        point = contour[0][0]
        for segment in contour:
            if len(segment) == 3:
                bcpin = segment[0]
                line(point, bcpin)

                point = segment[2]
                bcpout = segment[1]
                line(point, bcpout)
            else:
                point = segment[0]

    stroke(None)

    stroke(None)
    fill(0.3)
    for x, y in path.onCurvePoints:
        oval(x-r*1.5/2, y-r*1.5/2, r*1.5, r*1.5)

    stroke(None)
    fill(0.4)
    for x, y in path.offCurvePoints:
        rect(x-r/2, y-r/2, r, r)

CANVAS = 150
SIZE = 5
NUMBERS = 20

size(CANVAS, CANVAS)

getPath(u"/Users/shu/Downloads/nmm.ufo", "si-hira")

pen = BezierPath()

pen.moveTo((867, 353))
pen.curveTo((867, 388), (833, 401), (800, 401))
pen.curveTo((776, 401), (752, 395), (740, 385))
pen.curveTo((693, 348), (680, 289), (583, 232))
pen.curveTo((514, 192), (471, 178), (442, 178))
pen.curveTo((431, 178), (422, 181), (415, 184))
pen.curveTo((398, 193), (391, 223), (391, 261))
pen.curveTo((391, 302), (398, 353), (406, 398))
pen.curveTo((421, 486), (467, 581), (465, 601))
pen.curveTo((461, 644), (426, 667), (368, 667))
pen.curveTo((344, 667), (318, 660), (310, 628))
pen.curveTo((300, 588), (308, 581), (305, 566))
pen.curveTo((302, 551), (250, 290), (257, 237))
pen.curveTo((270, 138), (320, 69), (433, 69))
pen.curveTo((607, 69), (867, 284), (867, 353))
pen.closePath()

translate(12, (CANVAS - SIZE * NUMBERS) / 2)
fill(0.9)
stroke(0.9)
strokeWidth(1)
pen.scale(1/8)
drawPath(pen)

stroke(0.5)
strokeWidth(0.3)
drawHandle(pen, 1)

saveImage("/Users/shu/Downloads/nmm_si-hira.pdf")
# saveSketch("draw")