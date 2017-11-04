# sketch_helper

import os
import datetime
from drawBot import *
from robofab.world import *
from robofab.pens.pointPen import PrintingSegmentPen
from fontParts.nonelab import RFont

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
    filename = "/Users/shu/Downloads/" + filename + "_" + date
    suffix = 2

    if os.path.exists(filename + ".gif"):
        while os.path.exists(filename + "_" + str(suffix) + ".gif"):
            suffix += 1
        saveImage(filename + "_" + str(suffix) + ".gif")
    else:
        saveImage(filename + ".gif")

def savePNG(filename):

    date = str(datetime.date.today().strftime("%y%m%d"))
    filename = "/Users/shu/Downloads/" + filename + "_" + date
    suffix = 2

    if os.path.exists(filename + ".png"):
        while os.path.exists(filename + "_" + str(suffix) + ".png"):
            suffix += 1
        saveImage(filename + "_" + str(suffix) + ".png")
    else:
        saveImage(filename + ".png")

# quadratic bezier formula
def B1(t): return (1-t)*(1-t)
def B2(t): return 2*t*(1-t)
def B3(t): return t*t

def getBPoint(t, (x1, y1), (x2, y2), (x3, y3)):

    x = x1*B1(t) + x2*B2(t) + x3*B3(t)
    y = y1*B1(t) + y2*B2(t) + y3*B3(t)
    return x, y


# cubic bezier formula
def C1(t): return (1-t)*(1-t)*(1-t)
def C2(t): return 3*t*(1-t)*(1-t)
def C3(t): return 3*t*t*(1-t)
def C4(t): return t*t*t

def getCPoint(t, (x1, y1), (x2, y2), (x3, y3), (x4, y4)):

    x = x1*C1(t) + x2*C2(t) + x3*C3(t) + x4*C4(t)
    y = y1*C1(t) + y2*C2(t) + y3*C3(t) + y4*C4(t)
    return x, y

# generative process of cubic bezier
def getCProcess(t, (x1, y1), (x2, y2), (x3, y3), (x4, y4)):

    a1, i1 = x1 + (x2 - x1) * t, y1 + (y2 - y1) * t
    a2, i2 = x2 + (x3 - x2) * t, y2 + (y3 - y2) * t
    a3, i3 = x3 + (x4 - x3) * t, y3 + (y4 - y3) * t

    u1, e1 = a1 + (a2 - a1) * t, i1 + (i2 - i1) * t
    u2, e2 = a2 + (a3 - a2) * t, i2 + (i3 - i2) * t

    o, k = u1 + (u2 - u1) * t, e1 + (e2 - e1) * t

    return a1, i1, a2, i2, a3, i3, u1, e1, u2, e2, o, k

# colors
# cream = hexToRGB("FEF3DB")
# midnight = hexToRGB("353C5C")
# red = hexToRGB("E6333E")
# magenta = hexToRGB("E5326B")
# orange = hexToRGB("ED7B26")
# green = hexToRGB("44A87E")
# cyan = hexToRGB("41AFC9")
# blue = hexToRGB("3096F0")
# purple = hexToRGB("A94CBB")

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

    point_color = hexToRGB("A94CBB")
    handle_color = hexToRGB("41AFC9")

    stroke(None)

    fill(point_color[0], point_color[1], point_color[2])
    for x, y in path.onCurvePoints:
        oval(x-r, y-r, r*2, r*2)

    fill(handle_color[0], handle_color[1], handle_color[2])
    for x, y in path.offCurvePoints:
        rect(x-r/2, y-r/2, r, r)


def drawGlyph(x, y, sc, ufo, glyphs):

    font = RFont(ufo)
    UPM = font.info.unitsPerEm

    for g in glyphs:

        glyph = font[g]
        B = BezierPath()

        for contour in glyph:
            for i, segment in enumerate(contour):
                # curveTo
                if len(segment.points) == 3:
                    if i == 0:
                        if len(contour.segments[-1].points) == 3:
                            x, y = contour.segments[-1].points[2].x, contour.segments[-1].points[2].y
                        else:
                            x, y = contour.segments[-1].points[0].x, contour.segments[-1].points[0].y
                        B.moveTo((x, y))

                    x1, y1 = segment.points[0].x, segment.points[0].y
                    x2, y2 = segment.points[1].x, segment.points[1].y
                    x3, y3 = segment.points[2].x, segment.points[2].y
                    B.curveTo((x1, y1), (x2, y2), (x3, y3))

                # lineTo or moveTo
                else:
                    x, y = segment.points[0].x, segment.points[0].y
                    if i == 0:
                        B.moveTo((x, y))
                    else:
                        B.lineTo((x, y))

            B.closePath()

        B.scale(sc / UPM)

        translate(x, y)
        drawPath(B)

def getPath(ufo, glyph):
    font = RFont(ufo)
    g = font[glyph]
    pen = PrintingSegmentPen()
    g.draw(pen)

def getGlyphPath(glyph):
    glyph = glyph

    B = BezierPath()

    for contour in glyph:
        for i, segment in enumerate(contour):
            # curveTo
            if len(segment.points) == 3:
                if i == 0:
                    if len(contour.segments[-1].points) == 3:
                        x, y = contour.segments[-1].points[2].x, contour.segments[-1].points[2].y
                    else:
                        x, y = contour.segments[-1].points[0].x, contour.segments[-1].points[0].y
                    B.moveTo((x, y))

                x1, y1 = segment.points[0].x, segment.points[0].y
                x2, y2 = segment.points[1].x, segment.points[1].y
                x3, y3 = segment.points[2].x, segment.points[2].y
                B.curveTo((x1, y1), (x2, y2), (x3, y3))

            # lineTo or moveTo
            else:
                x, y = segment.points[0].x, segment.points[0].y
                if i == 0:
                    B.moveTo((x, y))
                else:
                    B.lineTo((x, y))

        B.closePath()

    return B
