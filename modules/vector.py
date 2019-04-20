#! /usr/bin/env python
# coding: utf-8
# vector.py
# 2019-04-20

import math

class Vector:
    def __init__(self, x = 1, y = 0):
        self.x = x
        self.y = y
        self.length = self._get_length()
        self.angle = self._get_angle()

    def set_x(self, x):
        self.x = x
        self.length = self._get_length()
        self.angle = self._get_angle()

    def set_y(self, y):
        self.y = y
        self.length = self._get_length()
        self.angle = self._get_angle()

    def _get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def _get_angle(self):
        return math.atan2(self.y, self.x)

    def set_angle(self, angle):
        length = self._get_length()
        self.angle = angle
        self.x = math.cos(angle) * length
        self.y = math.sin(angle) * length

    def set_length(self, length):
        angle = self._get_angle()
        self.length = length
        self.x = math.cos(angle) * length
        self.y = math.sin(angle) * length

    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)
    
    def __sub__(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)

    def __mul__(self, val):
        return Vector(self.x * val, self.y * val)
    
    def __div__(self, val):
        return Vector(self.x / val, self.y / val)

    def add(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)
    
    def subtract(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)

    def muliply(self, val):
        return Vector(self.x * val, self.y * val)
    
    def divide(self, val):
        return Vector(self.x / val, self.y / val)

    def add_to(self, v2):
        self.x += v2.x
        self.y += v2.y
        self.length = self._get_length()
        self.angle = self._get_angle()
    
    def subtract_from(self, v2):
        self.x -= v2.x
        self.y -= v2.y
        self.length = self._get_length()
        self.angle = self._get_angle()
    
    def muliply_by(self, val):
        self.x *= val
        self.y *= val
        self.length = self._get_length()
        self.angle = self._get_angle()
    
    def divide_by(self, val):
        self.x /= val
        self.y /= val
        self.length = self._get_length()
        self.angle = self._get_angle()

