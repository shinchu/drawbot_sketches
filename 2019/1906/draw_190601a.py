#! /usr/bin/env python
# coding: utf-8
# draw_190601a.py
# 2019-06-01

import os
import sys

mod_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../modules')
if mod_dir not in sys.path:
    sys.path.append(mod_dir)

import math
import random
import drawBot as db
from vector import Vector
from particle import Particle


db.newDrawing()

CANVAS = 500

fps = 50
sec = 14
total_frames = fps * sec
duration = 1 / fps

position = (CANVAS / 2, 0)

particles = []
n_particles = 100

for frame in range(total_frames):
    db.newPage(CANVAS, CANVAS)
    db.frameDuration(duration)

    db.stroke(None)

    if len(particles) < n_particles:
        p = Particle(*position, random.uniform(0, 1) * 8 + 5, math.pi / 2 + (random.uniform(0, 1) * 0.2 - 0.1), 0.1)
        p.radius = random.uniform(0, 1) * 5 + 5
        particles.append(p)

    for i, p in enumerate(particles):
        p.update()
        db.fill(i * 5 / CANVAS, (n_particles - i) * 5 / CANVAS, 0.7, 1)
        db.oval(p.position.x - p.radius, p.position.y - p.radius, p.radius * 2, p.radius * 2)

    if p.position.y - p.radius < 0:
        if frame < total_frames * 2 / 3:
            p.position.set_x(position[0])
            p.position.set_y(position[1])
            p.velocity.set_length(random.uniform(0, 1) * 8 + 5)
            p.velocity.set_angle(math.pi / 2 + (random.uniform(0, 1) * 0.2 - 0.1))
        elif frame == total_frames - 1:
            particles.clear()
        else:
            particles.remove(p)

# Save image
save_dir = os.path.expanduser('~/Downloads')
file_name = 'temp.gif'
db.saveImage(os.path.join(save_dir, file_name), imageResolution=144)

db.endDrawing()