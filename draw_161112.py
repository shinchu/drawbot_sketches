# drawbot 161112

from random import shuffle, choice
from sketch_helper import * 

CANVAS = 500

PSIZE = 35
NUMBERS = 10

grey = hexToRGB("333333")
white = hexToRGB("FFFFFF")

red = hexToRGB("E6333E")
magenda = hexToRGB("E5326B")
orange = hexToRGB("ED7B26")
cyan = hexToRGB("41AFC9")
blue = hexToRGB("3096F0")
purple = hexToRGB("A94CBB")
green = hexToRGB("44A87E")

colors = [red, magenda, orange, cyan, blue, purple, green]

size(CANVAS, CANVAS)

fill(grey[0], grey[1], grey[2])
rect(0, 0, CANVAS, CANVAS)

stroke(white[0], white[1], white[2])
fill(None)
drawGrid(CANVAS, CANVAS, PSIZE, NUMBERS)

pixel_addresses = [(4, 3), (5,3), (6, 3), (8, 3), (3, 4), (5, 4), (7, 4), (4, 5), (5, 5), (6, 5), (8, 5), (5, 6), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (5, 8)]
shuffle(pixel_addresses)

DURATION = 1 / 30

for i, address in enumerate(pixel_addresses):
    newPage(CANVAS, CANVAS)

    frameDuration(DURATION)

    fill(grey[0], grey[1], grey[2])
    rect(0, 0, CANVAS, CANVAS)

    stroke(white[0], white[1], white[2])
    fill(None)
    drawGrid(CANVAS, CANVAS, PSIZE, NUMBERS)

    fill(white[0], white[1], white[2])

    for j in range(i):
        drawPixel(CANVAS, CANVAS, PSIZE, NUMBERS, pixel_addresses[j])

    color = choice(colors)
    fill(color[0], color[1], color[2])
    drawPixel(CANVAS, CANVAS, PSIZE, NUMBERS, address)

    newPage(CANVAS, CANVAS)

    if i < len(pixel_addresses) - 1:
        frameDuration(DURATION)
    else:
        frameDuration(DURATION * 20)

    fill(grey[0], grey[1], grey[2])
    rect(0, 0, CANVAS, CANVAS)

    stroke(white[0], white[1], white[2])
    fill(None)
    drawGrid(CANVAS, CANVAS, PSIZE, NUMBERS)

    fill(white[0], white[1], white[2])

    for j in range(i + 1):
        drawPixel(CANVAS, CANVAS, PSIZE, NUMBERS, pixel_addresses[j])

saveSketch("draw")

