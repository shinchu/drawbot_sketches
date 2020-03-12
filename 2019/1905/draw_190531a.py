#! /usr/bin/env python
# coding: utf-8
# draw_190531a.py
# 2019-05-31

import os
import sys

mod_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../modules')
if mod_dir not in sys.path:  
    sys.path.append(mod_dir)

import math
import random
import drawBot as db
from vector import Vector
from particle import Particle


db.newDrawing()

CANVAS = 500

fps = 20
sec = 5
total_frames = fps * sec
duration = 1 / fps

sun = Particle(CANVAS / 2, CANVAS / 2, 0, 0)
planet = Particle(CANVAS / 2 + 100, CANVAS / 2, 15, -math.pi / 2)

sun.mass = 40000

sun_r = 20
planet_r = 5

sun_d = sun_r * 2
planet_d = planet_r * 2

for frame in range(total_frames):
    db.newPage(CANVAS, CANVAS)
    db.frameDuration(duration)

    planet.gravitate_to(sun)
    planet.update()

    db.stroke(0.8)
    db.fill(0.8)

    db.oval(sun.position.x - sun_r, sun.position.y - sun_r, sun_d, sun_d)
    db.oval(planet.position.x - planet_r, planet.position.y - planet_r, planet_d, planet_d)
    
# Save image
save_dir = os.path.expanduser('~/Downloads')
file_name = 'temp.gif'
db.saveImage(os.path.join(save_dir, file_name), imageResolution=144)

db.endDrawing()