#! /usr/bin/env python
# coding: utf-8
# particle.py
# 2019-04-20
#
import math
from vector import Vector

class Particle:
    def __init__(self, x, y, speed, direction, grav=0):
        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.velocity.set_length(speed)
        self.velocity.set_angle(direction)
        self.gravity = Vector(0, -grav) if grav else Vector(0, 0)
        self.mass = 1
    
    def accelerate(self, accel):
        self.velocity.add_to(accel)

    def update(self):
        self.velocity.add_to(self.gravity)
        self.position.add_to(self.velocity)

    def angle_to(self, p2):
        return math.atan2(p2.position.y - self.position.y, p2.position.x - self.position.x)
    
    def distance_to(self, p2):
        dx = p2.position.x - self.position.x
        dy = p2.position.y - self.position.y

        return math.sqrt(dx ** 2 + dy ** 2)
    
    def gravitate_to(self, p2):
        grav = Vector(0, 0)
        dist = self.distance_to(p2)

        grav.set_length(p2.mass / (dist ** 2))
        grav.set_angle(self.angle_to(p2))

        self.velocity.add_to(grav)
