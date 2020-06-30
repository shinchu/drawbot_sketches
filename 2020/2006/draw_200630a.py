#! /usr/bin/env python
# coding: utf-8
# draw_200630a.py
# 2020-06-30
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


def randomrange(minimum, maximum):
    return minimum + random.random() * (maximum - minimum)


class Triangle:
    def __init__(self, width, height, friction=0.9):
        self.particleA = Particle(randomrange(0, width),
                                  randomrange(0, height),
                                  randomrange(0, 50),
                                  randomrange(0, math.pi * 2))
        self.particleB = Particle(randomrange(0, width),
                                  randomrange(0, height),
                                  randomrange(0, 50),
                                  randomrange(0, math.pi * 2))

        self.particleC = Particle(randomrange(0, width),
                                  randomrange(0, height),
                                  randomrange(0, 50),
                                  randomrange(0, math.pi * 2))

        self.particleA.friction = friction
        self.particleB.friction = friction
        self.particleC.friction = friction

    def _spring(self, p0, p1, k=0.01, separation=20):
        distance = p0.position - p1.position
        distance.length -= separation
        spring_force = distance * k

        p1.velocity += spring_force
        p0.velocity -= spring_force

    def update(self):
        self._spring(self.particleA, self.particleB, k=0.02)
        self._spring(self.particleB, self.particleC)
        self._spring(self.particleC, self.particleA)

        self.particleA.update()
        self.particleB.update()
        self.particleC.update()

    def draw(self, r=10):
        db.oval(self.particleA.position.x - r, self.particleA.position.y - r, r * 2, r * 2)
        db.oval(self.particleB.position.x - r, self.particleB.position.y - r, r * 2, r * 2)
        db.oval(self.particleC.position.x - r, self.particleC.position.y - r, r * 2, r * 2)

        db.line((self.particleA.position.x, self.particleA.position.y), (self.particleB.position.x, self.particleB.position.y))
        db.line((self.particleB.position.x, self.particleB.position.y), (self.particleC.position.x, self.particleC.position.y))
        db.line((self.particleC.position.x, self.particleC.position.y), (self.particleA.position.x, self.particleA.position.y))


CANVAS = 500
fps = 30
sec = 3
frames = fps * sec
duration = 1 / fps

triangles = []
for _ in range(50):
    triangles.append(Triangle(CANVAS, CANVAS, random.random()))

for frame in tqdm(range(frames)):
    db.newPage(CANVAS, CANVAS)
    db.frameDuration(duration)

    db.fill(0)
    db.rect(0, 0, CANVAS, CANVAS)

    for triangle in triangles:
        triangle.update()

    db.stroke(1 - frame/frames)
    db.fill(1 - frame/frames)

    for triangle in triangles:
        triangle.draw(2)

db.saveImage('~/Downloads/draw.gif')