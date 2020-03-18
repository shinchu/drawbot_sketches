#! /usr/bin/env python
# coding: utf-8
# draw_200317a.py
# 2020-03-17
#
import os
import sys

mod_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../modules')
if mod_dir not in sys.path:
    sys.path.append(mod_dir)

import random
import math
from tqdm import tqdm
import drawBot as db
from particle import Particle

CANVAS = 500

fps = 50
sec = 30
frames = fps * sec
duration = 1 / fps

position = (CANVAS / 2, 0)

particles = []
n_particles = 200

for frame in tqdm(range(frames)):
    db.newPage(CANVAS, CANVAS)
    db.frameDuration(duration)

    db.stroke(None)

    if len(particles) < n_particles:
        if frame < frames / 2:
            p = Particle(*position, random.uniform(0, 1) * 8 + 5, math.pi / 2 + (random.uniform(0, 1) * 0.2 - 0.1), 0.15)
            p.radius = random.uniform(0, 1) * 5 + 5
            p.bounce = -0.9
            particles.append(p)

    for i, p in enumerate(particles):
        p.update()

        if frame < frames * 0.9:

            if p.position.x + p.radius > db.width():
                p.position.x = db.width() - p.radius
                p.velocity.x = p.velocity.x * p.bounce

            if p.position.x - p.radius < 0:
                p.position.x = p.radius
                p.velocity.x = p.velocity.x * p.bounce

            if p.position.y + p.radius > db.height():
                p.position.y = db.height() - p.radius
                p.velocity.y = p.velocity.y * p.bounce

            if p.position.y - p.radius < 0:
                p.position.y = p.radius
                p.velocity.y = p.velocity.y * p.bounce

        else:
            p.velocity.y += -20

        db.fill(i * 5 / CANVAS, (n_particles - i) * 5 / CANVAS, 0.7, 1)
        db.oval(p.position.x - p.radius, p.position.y - p.radius, p.diameter, p.diameter)

db.saveImage('~/Downloads/draw.gif')