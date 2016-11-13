# sketch_helper

import os
import datetime
from drawBot import rect, line, saveImage

def hexToRGB(hex_value):

    R = int(hex_value[0:2], 16) / float(255)
    G = int(hex_value[2:4], 16) / float(255)
    B = int(hex_value[4:6], 16) / float(255)

    color = (R, G, B)

    return color

def drawGrid(width, height, size, numbers):
    grid_width = size * numbers
    grid_height = size * numbers
    x = (width - grid_width) / 2
    y = (height - grid_height) / 2

    rect(x, y, grid_width, grid_height)

    i = 0

    while i < numbers:
        line((x + size * i, y), (x + size * i, y + grid_height))
        line((x, y + size * i), (x + grid_width, y + size * i))
        i += 1

def drawPixel(width, height, size, numbers, pixel_address):
    grid_width = size * numbers
    grid_height = size * numbers
    x = (width - grid_width) / 2
    y = (height - grid_height) / 2
    pixel_x, pixel_y = pixel_address

    rect(x + size * (pixel_x - 1), y + size * (pixel_y -1), size, size)

def saveSketch(filename):
    date = str(datetime.date.today().strftime("%y%m%d"))
    filename = filename + "_" + date
    suffix = 2

    if os.path.exists(filename + ".gif"):
        while os.path.exists(filename + "_" + str(suffix) + ".gif"):
            suffix += 1
        saveImage(filename + "_" + str(suffix) + ".gif")
    else:
        saveImage(filename + ".gif")
