#! /usr/bin/env python
# coding: utf-8
# draw_171104_a.py
# 2017-11-04
#
### Modules
# from drawBot import *
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))
from sketch_helper import *
from fontTools.pens.cocoaPen import CocoaPen

### Constants
CANVAS = 500
FPS = 30

RED = hexToRGB("E6333E")
MAGENTA = hexToRGB("E5326B")
ORANGE = hexToRGB("ED7B26")
GREEN = hexToRGB("44A87E")
CYAN = hexToRGB("41AFC9")
BLUE = hexToRGB("3096F0")
PURPLE = hexToRGB("A94CBB")
WHITE = (1, 1, 1)
BLACK = (0, 0, 0)
DARKGRAY = (0.1, 0.1, 0.1)

### Functions & procedures

def _drawGlyph(glyph):
    pen = CocoaPen(glyph.getParent())
    glyph.draw(pen)
    drawPath(pen.path)

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

# newDrawing()

### Variables

ufo = "/Users/shu/Downloads/Nemimi_Vanilla.ufo"
glyphs = ["mo-hira"]

font = RFont(ufo)
upm = font.info.unitsPerEm

sc = CANVAS / upm

### Instructions

for g in glyphs:

    glyph = font[g]
    xMin, yMin, xMax, yMax = glyph.box
    glyphWidth = glyph.width * sc
    glyphHeight = (yMax - yMin) * sc

    for i, t in enumerate([1/FPS * n for n in range(FPS+1)]):
        
        n = list(range(FPS+1))[i]

        newPage(CANVAS, CANVAS)
        fill(*BLACK)
        rect(0, 0, CANVAS, CANVAS)

        translate((CANVAS - glyphWidth)/2, (CANVAS - glyphHeight)/2)

        stroke(None)
        fill(*DARKGRAY)
        scale(sc)
        _drawGlyph(glyph)

        scale(1/sc)

        frameDuration(1/FPS)
        if n >= FPS-1:
            frameDuration(1)

        for contour in glyph:
            for i, segment in enumerate(contour):
                if len(segment.points) == 3:
                    if i == 0:
                        x1, y1 = contour.segments[-1].points[2].x, contour.segments[-1].points[2].y
                    else:
                        if len(contour.segments[i-1].points) == 3:
                            x1, y1 = contour.segments[i-1].points[2].x, contour.segments[i-1].points[2].y
                        else:
                            x1, y1 = contour.segments[i-1].points[0].x, contour.segments[i-1].points[0].y

                    x2, y2 = segment.points[0].x, segment.points[0].y
                    x3, y3 = segment.points[1].x, segment.points[1].y
                    x4, y4 = segment.points[2].x, segment.points[2].y

                else:
                    if i == 0:
                        x1, y1 = contour.segments[-1].points[0].x, contour.segments[-1].points[0].y
                    else:
                        if len(contour.segments[i-1].points) == 3:
                            x1, y1 = contour.segments[i-1].points[2].x, contour.segments[i-1].points[2].y
                        else:
                            x1, y1 = contour.segments[i-1].points[0].x, contour.segments[i-1].points[0].y

                    x4, y4 = segment.points[0].x, segment.points[0].y
                    x2, y2 = x1, y1
                    x3, y3 = x4, y4

                x1, y1 = x1 * sc , y1 * sc
                x2, y2 = x2 * sc , y2 * sc
                x3, y3 = x3 * sc , y3 * sc
                x4, y4 = x4 * sc , y4 * sc

                a1, i1, a2, i2, a3, i3, u1, e1, u2, e2, o, k = getCProcess(t, (x1, y1), (x2, y2), (x3, y3), (x4, y4))

                for t2 in [1/FPS * n for n in range(int(t*FPS) + 1)]:

                    a1, i1, a2, i2, a3, i3, u1, e1, u2, e2, o, k = getCProcess(t2, (x1, y1), (x2, y2), (x3, y3), (x4, y4))
                    strokeWidth(2)
                    stroke(*PURPLE)
                    line((a1, i1), (a2, i2))
                    stroke(*ORANGE)
                    line((a2, i2), (a3, i3))

                    strokeWidth(2)
                    stroke(*MAGENTA)
                    line((u1, e1), (u2, e2))

                strokeWidth(2)
                stroke(*WHITE)
                line((x1, y1), (x2, y2))
                line((x2, y2), (x3, y3))
                line((x3, y3), (x4, y4))

        pen = getGlyphPath(glyph)
        pen.scale(sc)

        for point in pen.onCurvePoints:
            x, y = point[0], point[1]
            d = 8
            fill(*WHITE)
            stroke(None)
            oval(x-d/2, y-d/2, d, d)

saveSketch("draw")
# endDrawing()