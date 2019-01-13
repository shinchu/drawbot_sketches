#! /usr/bin/env python
# coding: utf-8
# draw_181231_a.py
# 2018-12-31
#
import os
import sys
import math
import random
sys.path.append(os.path.dirname(os.getcwd()))

import drawBot as db
import sketch_helper as sh

CANVAS = (500, 500)
FRAMES = 30

ufo_path = '/Users/shu/Dropbox/Life/Misc/nenga_2019/pig_2018.ufo'

if __name__ == "__main__":

    db.newDrawing()

    db.size(*CANVAS)
    
    glyphs = ['A', 'B', 'C', 'D', 'E', 'F']
    
    pig_outline = sh.getGlyphPath(ufo_path, 'A')
    min_x, min_y, max_x, max_y = pig_outline.bounds()
    width = (max_x - min_x)
    height = (max_y - min_y)
    
    scale = 0.1
    margin = 20
    
    vertical_pigs = math.floor(CANVAS[1] / ((height + margin / 2) * scale))
    horizontal_pigs = math.floor(CANVAS[0] / ((width + margin) * scale))
    
#    for k in range(FRAMES):
        # db.newPage(*CANVAS)
        # db.frameDuration(1/FRAMES)
    db.save()
    db.scale(scale)
    y = -height
    for i in range(vertical_pigs + 2):
        x = -width
        for j in range(horizontal_pigs + 2):
            db.save()
            db.translate(x, y)
            pig = sh.getGlyphPath(ufo_path, random.choice(glyphs))
            # db.fill(j / random.randint(10, 15), i / random.randint(20, 30), random.uniform(0.6, 0.8), 1)
            db.fill(j / 15, i / 20, 0.7, 1)
            db.drawPath(pig)
            db.restore()
            x += width + margin
        y += height
    db.restore()

    db.fill(1)

    db.font('Cooper Std Black', 150)
    db.text('2019', (60, 200))

    db.saveImage('~/Downloads/pig.gif', imageResolution=300)
    db.endDrawing()