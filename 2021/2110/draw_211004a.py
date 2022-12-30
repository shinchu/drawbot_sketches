#! /usr/bin/env python
# coding: utf-8
# draw_211004a.py
# 2021-10-04
#

import os
import sys
import math
from tqdm import tqdm
import drawBot as db

mod_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../modules')
if mod_dir not in sys.path:
    sys.path.append(mod_dir)

import matrix_calc as matc


def connect(i, j, points):
    a = points[i]
    b = points[j]
    db.stroke(0)
    db.strokeWidth(4)
    db.line(a, b)


FRAMES = 420
CANVAS = 500
angle = 0
projection = [[1, 0, 0],
              [0, 1, 0]]
points = [(-0.433, 0, -0.25),
          (0.433, 0, -0.25),
          (0, 0, 0.5),
          (0, 0.56, 0),
          (0, -0.56, 0),
          (0, 0, 0)]


for frame in tqdm(range(FRAMES)):

    db.newPage(CANVAS, CANVAS)
    db.frameDuration(1/50)
    db.translate(CANVAS/2, CANVAS/2)

    rotationZ = [[math.cos(angle), -math.sin(angle), 0],
                 [math.sin(angle), math.cos(angle), 0],
                 [0, 0, 1]]

    rotationX = [[1, 0, 0],
                 [0, math.cos(angle), -math.sin(angle)],
                 [0, math.sin(angle), math.cos(angle)]]
 
    rotationY = [[math.cos(angle), 0, -math.sin(angle)],
                 [0, 1, 0],
                 [math.sin(angle), 0, math.cos(angle)]]
    
    projected = []         
    for point in points:
        rotated = matc.matmul(rotationZ, matc.vec_to_mat(point))
        rotated = matc.matmul(rotationX, matc.vec_to_mat(rotated))
        rotated = matc.matmul(rotationY, matc.vec_to_mat(rotated))
        
        projected2d = matc.matmul(projection, matc.vec_to_mat(rotated))
        projected2d = tuple([x * 130 for x in projected2d])
        projected.append(projected2d)
    
    if frame < FRAMES / 2:
        db.stroke((frame / FRAMES), 1 - (frame / FRAMES), 1 - (frame / FRAMES))
        db.fill((frame / FRAMES), 1 - (frame / FRAMES), 1 - (frame / FRAMES))
    else:
        db.stroke(1 - (frame / FRAMES), (frame / FRAMES), (frame / FRAMES))
        db.fill(1 - (frame / FRAMES), (frame / FRAMES), (frame / FRAMES))


    for i in range(3):
        connect(i, (i + 1) % 3, projected)
        connect(i, 3, projected)
        connect(i, 4, projected)

    angle += 0.020
    
db.saveImage("~/Downloads/draw.gif")