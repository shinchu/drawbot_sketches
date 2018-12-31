#! /usr/bin/env python
# coding: utf-8
# draw_171102_a.py
# 2017-11-02
#
# from drawBot import *
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))
from sketch_helper import *

# newDrawing()

size(500, 500)
x1, y1 = 50, 120
x2, y2 = 225, 300
x3, y3 = 400, 120

stroke(0)
line((x1, y1), (x2, y2))
line((x2, y2), (x3, y3))

for t in [0.2 * n for n in range(6)]:

    m1, k1 = x1 + (x2-x1) * t, y1 + (y2-y1) * t
    m2, k2 = x2 + (x3-x2) * t, y2 + (y3-y2) * t

    line((m1, k1), (m2, k2))

newPage(500, 500)
x1, y1 = 50, 120
x2, y2 = 150, 300
x3, y3 = 300, 300
x4, y4 = 400, 120

stroke(0)
line((x1, y1), (x2, y2))
line((x2, y2), (x3, y3))
line((x3, y3), (x4, y4))

for t in [0.2 * n for n in range(6)]:

    m1, k1 = x1 + (x2-x1) * t, y1 + (y2-y1) * t
    m2, k2 = x2 + (x3-x2) * t, y2 + (y3-y2) * t
    m3, k3 = x3 + (x4-x3) * t, y3 + (y4-y3) * t

    line((m1, k1), (m2, k2))
    line((m2, k2), (m3, k3))

    a1, b1 = m1 + (m2-m1) * t, k1 + (k2-k1) * t
    a2, b2 = m2 + (m3-m2) * t, k2 + (k3-k2) * t

    e, f = a1 + (a2-a1) * t, b1 + (b2-b1) * t

    line((a1, b1), (a2, b2))

    # x, y = getCPoint(t, (x1, y1), (x2, y2), (x3, y3), (x4, y4))

    # oval(e - 3, f - 3, 6, 6)

# endDrawing()
