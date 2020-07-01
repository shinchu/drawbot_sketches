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


class Walker:
    def __init__(self, width, height, margin=50):
        self.x = width / 2
        self.y = height / 2
        self.history = [(self.x, self.y)]

    def draw(self, distance=10):
        directions = ["E", "W", "S", "N"]
        direction = random.choice(directions)

        if len(self.history) > 1:
            for p0, p1 in zip(self.history[0:], self.history[1:]):
                db.line(p0, p1)

        if direction == "E":
            db.line((self.x, self.y), (self.x + distance, self.y))
            self.x += distance
        elif direction == "W":
            db.line((self.x, self.y), (self.x - distance, self.y))
            self.x -= distance
        elif direction == "S":
            db.line((self.x, self.y), (self.x, self.y - distance))
            self.y -= distance
        elif direction == "N":
            db.line((self.x, self.y), (self.x, self.y + distance))
            self.y += distance

        self.history.append((self.x, self.y))


CANVAS = 500
fps = 20
sec = 3
frames = fps * sec
duration = 1 / fps

walkers = []
for _ in range(200):
    walkers.append(Walker(CANVAS, CANVAS))

for frame in tqdm(range(frames)):
    db.newPage(CANVAS, CANVAS)
    db.frameDuration(duration)
    if frame == frames - 1:
        db.frameDuration(duration * 10)

    db.fill(0)
    db.rect(0, 0, CANVAS, CANVAS)

    db.stroke(1 - frame/frames, 0, frame/frames, 1 - frame/frames)

    for walker in walkers:
        walker.draw(5)

db.saveImage('~/Downloads/draw.gif')