#! /usr/bin/env python
# coding: utf-8
# draw_171103_b.py
# 2017-11-03
#
# from drawBot import *
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))
from sketch_helper import *
from fontTools.pens.cocoaPen import CocoaPen

# newDrawing()

def _drawGlyph(glyph):
    pen = CocoaPen(glyph.getParent())
    glyph.draw(pen)
    drawPath(pen.path)

ufo = u"/Users/shu/Downloads/Nemimi_Original.ufo"
glyphs = ["M"]

# colors
cream = hexToRGB("FEF3DB")
midnight = hexToRGB("353C5C")
red = hexToRGB("E6333E")
magenta = hexToRGB("E5326B")
orange = hexToRGB("ED7B26")
green = hexToRGB("44A87E")
cyan = hexToRGB("41AFC9")
blue = hexToRGB("3096F0")
purple = hexToRGB("A94CBB")

CANVAS = 500

font = RFont(ufo)
UPM = font.info.unitsPerEm

sc = CANVAS / UPM

for g in glyphs:

    glyph = font[g]
    xMin, yMin, xMax, yMax = glyph.box
    glyphWidth = glyph.width * sc
    glyphHeight = (yMax - yMin) * sc
    
    for t in [0.05 * n for n in range(21)]:
        
        newPage(CANVAS, CANVAS)
        fill(0)
        rect(0, 0, CANVAS, CANVAS)

        translate((CANVAS - glyphWidth)/2, (CANVAS - glyphHeight)/2)
        
        stroke(None)
        fill(red[0], red[1], red[2])
        scale(sc)
        _drawGlyph(glyph)
        
        scale(1/sc)
        
        frameDuration(1/12)
        if n == 19:
            frameDuration(1)
        if n > 19:
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
                        
                for t2 in [0.05 * n for n in range(int(t/0.05) + 1)]:
                
                    # strokeWidth(2)
                    # stroke(1)
                    # line((x1, y1), (x2, y2))
                    # line((x2, y2), (x3, y3))
                    # line((x3, y3), (x4, y4))
                
                    a1, i1, a2, i2, a3, i3, u1, e1, u2, e2, o, k = getCProcess(t2, (x1, y1), (x2, y2), (x3, y3), (x4, y4))
                    strokeWidth(2)
                    stroke(purple[0], purple[1], purple[2])
                    line((a1, i1), (a2, i2))
                    stroke(blue[0], blue[1], blue[2])
                    line((a2, i2), (a3, i3))
                    
                    strokeWidth(2)
                    stroke(green[0], green[1], green[2])
                    line((u1, e1), (u2, e2))
               
                strokeWidth(3)
                stroke(1)
                line((x1, y1), (x2, y2))
                line((x2, y2), (x3, y3))
                line((x3, y3), (x4, y4))  
               
                # stroke(1)
                # fill(1)
                # d = 6
                # oval(o - d/2, k - d/2, d, d) 
                
saveSketch("draw")
# endDrawing()