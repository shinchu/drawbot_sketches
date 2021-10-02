#! /usr/bin/env python
# coding: utf-8
# draw_210501a.py
# 2021-05-01
#
import os
import sys

mod_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../modules')
if mod_dir not in sys.path:
    sys.path.append(mod_dir)

import random
from tqdm import tqdm
import drawBot as db
from triangle import Triangle


CANVAS = 500
fps = 30
sec = 5
frames = fps * sec
duration = 1 / fps

triangles = []
for _ in range(50):
    triangles.append(Triangle(CANVAS, CANVAS, random.random()))

for frame in tqdm(range(frames)):
    db.newPage(CANVAS, CANVAS)
    db.frameDuration(duration)
    if frame == frames - 1:
        db.frameDuration(duration * 2)

    db.fill(1)
    db.rect(0, 0, CANVAS, CANVAS)

    for triangle in triangles:
        if frame < frames / 2:
            triangle.update(k=0.03)
        else:
            triangle.replay()

    db.stroke(0)
    db.fill(0)

    for triangle in triangles:
        triangle.draw(2)

db.saveImage('~/Downloads/draw.gif')