#! /usr/bin/env python
# coding: utf-8
# draw_200316.py
# 2020-03-16
#

CANVAS = 500

fps = 30
seconds = 5
frames = fps * seconds
duration = 1 / fps

for frame in range(frames):
    newPage(CANVAS, CANVAS)
    frameDuration(duration)

    stroke(0)
    strokeWidth(1)
    
    if frame < frames / 2:
        bars = CANVAS/100 + (CANVAS/2 - CANVAS/100) * frame / frames
    else:
        bars = CANVAS/100 + (CANVAS/2 - CANVAS/100) * (frames - frame) / frames

    n_bars = int(CANVAS // bars)

    for i in range(n_bars):
        line((i * bars, height()), ((i + 1) * bars, 0))
        line((i * bars, 0), ((i + 1) * bars, height()))
        line((0, i * bars), (width(), (i + 1) * bars))
        line((width(), i * bars), (0, (i + 1) * bars))

saveImage('~/Downloads/draw.gif', imageResolution=144)