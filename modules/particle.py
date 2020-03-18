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
        self.velocity.length = speed
        self.velocity.angle = direction
        self.gravity = Vector(0, -grav)
        self.mass = 1
        self.radius = 0
        self.bounce = -1
        self.friction = 1

    def __repr__(self):
        return 'Particle(position={}, velocity={}, gravity={})'.format(self.position, self.velocity, self.gravity)

    def __str__(self):
        return 'Particle(position={}, velocity={}, gravity={})'.format(self.position, self.velocity, self.gravity)

    @property
    def diameter(self):
        return self.radius * 2

    def accelerate(self, accel):
        self.velocity += accel

    def update(self):
        self.velocity *= self.friction
        self.velocity += self.gravity
        self.position += self.velocity

    def angle_to(self, p2):
        return math.atan2(p2.position.y - self.position.y, p2.position.x - self.position.x)

    def distance_to(self, p2):
        dx = p2.position.x - self.position.x
        dy = p2.position.y - self.position.y

        return math.sqrt(dx ** 2 + dy ** 2)

    def gravitate_to(self, p2):
        grav = Vector(0, 0)
        dist = self.distance_to(p2)

        grav.length = p2.mass / (dist ** 2)
        grav.angle = self.angle_to(p2)

        self.velocity += grav
