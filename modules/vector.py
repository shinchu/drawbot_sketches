#! /usr/bin/env python
# coding: utf-8
# vector.py
# 2019-04-20

import math

class Vector:
    def __init__(self, x = 1, y = 0):
        self.__x = x
        self.__y = y
        self.__length = self.length
        self.__angle = self.angle

    def __repr__(self):
        return 'Vector(x={}, y={}, length={}, angle={})'.format(self.x, self.y, self.length, self.angle)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    @length.setter
    def length(self, value):
        self.__length = value
        self.update()

    @angle.setter
    def angle(self, value):
        self.__angle = value
        self.update()

    def update(self):
        self.x = math.cos(self.__angle) * self.__length
        self.y = math.sin(self.__angle) * self.__length

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

    def multiply(self, val):
        return Vector(self.x * val, self.y * val)

    def divide(self, val):
        return Vector(self.x / val, self.y / val)

    def add_to(self, v2):
        self.x += v2.x
        self.y += v2.y

    def subtract_from(self, v2):
        self.x -= v2.x
        self.y -= v2.y

    def multiply_by(self, val):
        self.x *= val
        self.y *= val

    def divide_by(self, val):
        self.x /= val
        self.y /= val

