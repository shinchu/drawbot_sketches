#! /usr/bin/env python
# coding: utf-8
# draw_171103_a.py
# 2017-11-03
#
# from drawBot import *
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))
from sketch_helper import *

# newDrawing()

x1, y1 = 100, 120
x2, y2 = 20, 600
x3, y3 = 450, 300
x4, y4 = 100, 120

for t in [0.05 * n for n in range(21)]:
    newPage(500, 500)
    frameDuration(1/10)
    if n == 19:
        frameDuration(1)
    
    stroke(0)
    line((x1, y1), (x2, y2))
    line((x2, y2), (x3, y3))
    line((x3, y3), (x4, y4))
    
    for t2 in [0.05 * n for n in range(int(t/0.05) + 1)]:

        a1, i1, a2, i2, a3, i3, u1, e1, u2, e2, o, k = getCProcess(t2, (x1, y1), (x2, y2), (x3, y3), (x4, y4))

        stroke(0)

        line((a1, i1), (a2, i2))
        line((a2, i2), (a3, i3))

        line((u1, e1), (u2, e2))

        oval(o - 3, k - 3, 6, 6)

saveImage("/Users/shu/Downloads/temp.gif")
# endDrawing()