# drawbot 161116

from random import choice
from sketch_helper import *

CANVAS = 500
NUMBERS = 10
FRAMES = 25
DURATION = 1 / 20
X = 110
Y = 90
H = 50
MARGIN = 30

cream = hexToRGB("FEF3DB")
midnight = hexToRGB("353C5C")
red = hexToRGB("E6333E")
magenda = hexToRGB("E5326B")
orange = hexToRGB("ED7B26")
cyan = hexToRGB("41AFC9")
blue = hexToRGB("3096F0")
purple = hexToRGB("A94CBB")
green = hexToRGB("44A87E")

colors = [red, magenda, orange, cyan, blue, purple, green, cream, purple]

B = BezierPath()
B.moveTo((X - MARGIN, Y - MARGIN))
B.lineTo((X - MARGIN, Y - MARGIN + H))

for n in range(FRAMES):
    
    newPage(CANVAS, CANVAS)
    frameDuration(DURATION)
    if n < FRAMES/2:
        strokeWidth(n + 1)
    else:
        strokeWidth(FRAMES - n)

    for i in range(NUMBERS):

        if i % 2 == 1:
            translate(-MARGIN/2, MARGIN)
        else:
            translate(MARGIN/2, MARGIN)

        save()
    
        for j in range(NUMBERS):
            translate(MARGIN, 0)
            color = choice(colors)
            stroke(color[0], color[1], color[2])
            drawPath(B)
        
        restore()
    
saveSketch("draw")