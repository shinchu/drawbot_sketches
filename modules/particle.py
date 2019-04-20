#! /usr/bin/env python
# coding: utf-8
# particle.py
# 2019-04-20
#
from vector import Vector

class Particle:
    def __init__(self, x, y, speed, direction, grav):
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.velocity.set_length(speed)
        self.velocity.set_angle(direction)
        self.gravity = Vector(0, -grav) if grav else Vector(0, 0)
    
    def accelerate(self, accel):
        self.velocity.add_to(accel)

    def update(self):
        self.velocity.add_to(self.gravity)
        self.position.add_to(self.velocity)