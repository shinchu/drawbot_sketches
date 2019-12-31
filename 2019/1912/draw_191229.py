#! /usr/bin/env python
# coding: utf-8
# draw_191229.py
# 2019-12-29
#

import sys
import os
import math
import random

mod_dir = os.path.expanduser('~/.virtualenvs/drawbot_sketches-Cz4vd33r/lib/python3.7/site-packages')

if mod_dir not in sys.path:
    sys.path.append(mod_dir)

import numpy as np
import drawBot as db

def draw_textile(mtx, tate_color, yoko_color, grid_size=10):

    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[1]):
            if mtx[i][j] == 1:
                db.stroke(*tate_color)
                db.fill(*tate_color)
            elif mtx[i][j] == 0:
                db.stroke(*yoko_color)
                db.fill(*yoko_color)

            db.rect(i * grid_size, j * grid_size , grid_size, grid_size)


def append_textile(mtx, width, height):

    for i in range(width):
        mtx = np.hstack([mtx, mtx])

    for i in range(height):
        mtx = np.vstack([mtx, mtx])

    return mtx


def generate_textile(row_A, column_A, random_seed=2020, sym=True):

    random.seed(random_seed)

    mtx_A1 = np.zeros((row_A, column_A))
    mtx_B = np.random.randint(2, size=(column_A, column_A))

    for i in range(row_A):
        if (int(i / column_A) % 2 == 0):
            zigzag = i % column_A
        else:
            zigzag = column_A - (i % column_A) - 1

        mtx_A1[i][zigzag] = 1

    mtx_A2 = np.flipud(mtx_A1).copy()
    mtx_C1 = mtx_A1.copy()
    mtx_C2 = np.fliplr(mtx_C1).copy()

    if sym:
        for i in range(column_A):
            for j in range(i, column_A):
                mtx_B[i][j] = mtx_B[i][j]

    mtx_P11 = np.dot(mtx_A1.transpose(), np.dot(mtx_B, mtx_C1))
    mtx_P12 = np.dot(mtx_A1.transpose(), np.dot(mtx_B, mtx_C2))
    mtx_P21 = np.dot(mtx_A2.transpose(), np.dot(mtx_B, mtx_C1))
    mtx_P22 = np.dot(mtx_A2.transpose(), np.dot(mtx_B, mtx_C2))

    mtx_P1 = np.hstack([mtx_P11, mtx_P12])
    mtx_P2 = np.hstack([mtx_P21, mtx_P22])

    mtx_P = np.vstack([mtx_P1, mtx_P2])

    return mtx_P

db.newDrawing()

CANVAS = 500

fps = 15
sec = 4
total_frames = fps * sec
duration = 1 / fps

mtx = generate_textile(10, 10, random_seed=2020, sym=True)
mtx = append_textile(mtx, 3, 3)

for frame in range(total_frames):
    db.newPage(CANVAS, CANVAS)
    if frame == 0:
        db.frameDuration(4 * duration)
    else:
        db.frameDuration(duration)

    tate_color = (1 - math.sin(frame / 5), 1 - math.sin(frame / 10), 1 - math.sin(frame / 100))
    yoko_color = (0, 0, 0)

    draw_textile(mtx, tate_color, yoko_color, grid_size=5)

# Save image
save_dir = os.path.expanduser('~/Downloads')
file_name = 'temp.gif'
db.saveImage(os.path.join(save_dir, file_name), imageResolution=144)

db.endDrawing()