#! /usr/bin/env python
# coding: utf-8
# draw_190420a.py
# 2019-04-20

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
sec = 5
total_frames = fps * sec
duration = 1 / fps

position = (CANVAS / 2, CANVAS * 2 / 3)
d = 15
r = d / 2

particles = []
n_particles = 100

for i in range(n_particles):
    particles.append(Particle(*position, random.uniform(0, 1) * 6 + 1, random.uniform(0, 1) * 2 * math.pi, 0.1))

for frame in range(total_frames):
    db.newPage(CANVAS, CANVAS)
    db.frameDuration(duration)
 
    db.stroke(0.8)
    db.fill(0.8)
    
    for i in range(n_particles):
        p = particles[i]
        p.update()
        db.oval(p.position.x - r, p.position.y - r, d, d)
    
# Save image
save_dir = os.path.expanduser('~/Downloads')
file_name = 'temp.gif'
db.saveImage(os.path.join(save_dir, file_name), imageResolution=144)

db.endDrawing()