# drawbot 170426

from sketch_helper import *

CANVAS = 500
PSIZE = 35
NUMBERS = 10
DURATION = 1 / 30

size(CANVAS, CANVAS)

fill(None)
rect(0, 0, CANVAS, CANVAS)

stroke(0)
drawGrid(CANVAS, CANVAS, PSIZE, NUMBERS)

pixel_addresses = [
    (4, 5), (4, 6), (5, 4), (5, 7), (6, 4), (6, 7), (7, 1), (7, 2), (7, 3),
    (7, 4), (7, 5), (7, 6), (8, 1)
    ]

for i, address in enumerate(pixel_addresses):
    newPage(CANVAS, CANVAS)
    frameDuration(DURATION)

    fill(None)
    rect(0, 0, CANVAS, CANVAS)

    stroke(0)
    drawGrid(CANVAS, CANVAS, PSIZE, NUMBERS)

    fill(0)

    for j in range(i + 1):
        drawPixel(CANVAS, CANVAS, PSIZE, NUMBERS, pixel_addresses[j])


# saveSketch("draw")
