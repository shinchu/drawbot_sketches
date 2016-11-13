# drawbot 161112

import random
from sketch_helper import hexToRGB, drawGrid, drawPixel, saveSketch


if __name__ == "__main__":

    width, height = 500, 500

    pixel_size = 35
    numbers = 10

    grey = hexToRGB("333333")
    white = hexToRGB("FFFFFF")

    cream = hexToRGB("FEF3DB")
    midnight = hexToRGB("353C5C")

    red = hexToRGB("E6333E")
    magenda = hexToRGB("E5326B")
    orange = hexToRGB("ED7B26")
    cyan = hexToRGB("41AFC9")
    blue = hexToRGB("3096F0")
    purple = hexToRGB("A94CBB")
    green = hexToRGB("44A87E")

    colors = [red, magenda, orange, cyan, blue, purple, green]
    
    size(width, height)

    fill(grey[0], grey[1], grey[2])
    rect(0, 0, width, height)

    stroke(white[0], white[1], white[2])
    fill(None)
    drawGrid(width, height, pixel_size, numbers)

    pixel_addresses = [(4, 3), (5,3), (6, 3), (8, 3), (3, 4), (5, 4), (7, 4), (4, 5), (5, 5), (6, 5), (8, 5), (5, 6), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (5, 8)]
    random.shuffle(pixel_addresses)

    duration = 1 / 30

    for i, address in enumerate(pixel_addresses):
        newPage(width, height)

        frameDuration(duration)

        fill(grey[0], grey[1], grey[2])
        rect(0, 0, width, height)

        stroke(white[0], white[1], white[2])
        fill(None)
        drawGrid(width, height, pixel_size, numbers)

        fill(white[0], white[1], white[2])

        for j in range(i):
            drawPixel(width, height, pixel_size, numbers, pixel_addresses[j])

        color = random.choice(colors)
        fill(color[0], color[1], color[2])
        drawPixel(width, height, pixel_size, numbers, address)

        newPage(width, height)

        if i < len(pixel_addresses) - 1:
            frameDuration(duration)
        else:
            frameDuration(duration * 20)

        fill(grey[0], grey[1], grey[2])
        rect(0, 0, width, height)

        stroke(white[0], white[1], white[2])
        fill(None)
        drawGrid(width, height, pixel_size, numbers)

        fill(white[0], white[1], white[2])

        for j in range(i + 1):
            drawPixel(width, height, pixel_size, numbers, pixel_addresses[j])

    saveSketch("draw")

