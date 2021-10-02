#! /usr/bin/env python
# coding: utf-8
# draw_210627a.py
# 2021-06-27
#

import random
import math
from tqdm import tqdm
import drawBot as db
from perlin_noise import PerlinNoise

CANVAS = 500
FPS = 30
DURATION = 3
FRAMES = FPS * DURATION


for frame in tqdm(range(FRAMES)):

    db.newPage(CANVAS, CANVAS)
    # Ai-iro
    db.fill(0, 76/255, 113/255)
    db.stroke(None)
    db.rect(0, 0, CANVAS, CANVAS)

    path_above = db.BezierPath()
    path_below = db.BezierPath()
    noise1 = PerlinNoise(octaves=FRAMES - frame, seed=55)
    noise2 = PerlinNoise(octaves=frame + 1, seed=30)

    for i in range(0, 2000):
    
        if i == 0:
            path_below.moveTo((0, CANVAS))
            path_above.moveTo((0, 0))
    
        if i == 1:
            x1, y1 = 0, 50
            x2, y2 = 0, 80
            path_below.lineTo((x1, y1))
            path_above.lineTo((x2, y2))
    
        new_x1 = i / 360 * CANVAS
        new_y1 = 50 + noise1(i/1000) + 30 * math.sin(math.radians(i))
    
        new_x2 = i / 360 * CANVAS
        new_y2 = 80 + noise2(i/60) + 30 * math.sin(math.radians(i))
        
        path_below.lineTo((new_x1, new_y1))
        path_above.lineTo((new_x2, new_y2))
    
        x1, y1 = new_x1, new_y1
        x2, y2 = new_x2, new_y2

    path_below.lineTo((x1, CANVAS))
    path_above.lineTo((x2, 0))

    path_below.closePath()
    path_above.closePath()

    wave = path_above.intersection(path_below)

    db.fill(1)

    whole = db.BezierPath()

    db.translate(0, -1000)
    db.rotate(45)
    for i in range(20):
        db.translate(0, 50)
        db.drawPath(wave)

db.saveImage('~/Downloads/draw.gif')