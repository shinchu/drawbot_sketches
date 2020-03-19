#! /usr/bin/env python
# coding: utf-8
# draw_200319a.py
# 2020-03-19
#
import math

CANVAS = 500

n_cols = 10
n_rows = 10
margin = 18
line_height = 12
pole_height = 10
pole_width = 2

h = n_rows * min(line_height, pole_height)
w = (n_cols - 2) * margin + 0.5 * margin * n_cols

fps = 20
sec = 6
frames = fps * sec
duration = 1 / fps

for frame in range(frames):
    newPage(CANVAS, CANVAS)
    frameDuration(duration)
    
    stroke(0.8)
    fill(0.8)
    rect(0, 0, width(), height())

    translate((width() - w) / 2, (height() - h) / 2)
    
    stroke(0)
    strokeWidth(pole_width)
    lineCap('round')

    for i in range(n_cols):
        for j in range(n_rows):
            line((j * margin + i * 0.5 * margin, i * line_height + 0.5 * line_height * math.sin(math.pi + j + i + frame / 19)), (j * margin + i * 0.5 * margin, i * line_height + pole_height + 0.5 * line_height * math.sin(math.pi + j + i + frame / 19)))
            
saveImage('~/Downloads/draw.gif')