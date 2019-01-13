#! /usr/bin/env python
# coding: utf-8
# draw_190114.py
# 2019-01-14
#
import os
import sys
import math
import random
sys.path.append(os.path.dirname(os.getcwd()))

import drawBot as db
import sketch_helper as sh


def make_box(box_size, box_depth):
        
    box = db.BezierPath()
    box.moveTo((box_size[0], 0))
    box.lineTo((0, 0))
    box.lineTo((0, box_size[1]))
    box.lineTo((box_size[0], box_size[1]))
    box.closePath()
    box.moveTo((0, 0))
    box.lineTo((box_depth[0], box_depth[1]))
    box.lineTo((box_depth[0], box_size[1] + box_depth[1]))
    box.lineTo((0, box_size[1]))
    box.closePath()
    box.moveTo((box_depth[0], box_size[1] + box_depth[1]))
    box.lineTo((box_size[0] + box_depth[0], box_size[1] + box_depth[1]))
    box.lineTo((box_size[0], box_size[1]))
    box.lineTo((0, box_size[1]))
    box.closePath()
        
    return box


def draw_block(box_size, box_depth, rows, columns, layers):
    
    box = make_box(box_size, box_depth)
    
    for column in range(columns):
        db.save()
        db.translate(-column * box_size[0], 0)
        db.drawPath(box)
        for row in range(rows):
            db.save()
            db.translate(0, row * box_size[1])
            db.drawPath(box)
            for layer in range(layers - 1):
                db.translate(math.fabs(box_depth[0]), -math.fabs(box_depth[1]))
                db.drawPath(box)
            db.restore()
        db.restore()
    

if __name__ == "__main__":
    
    db.newDrawing()
    
    CANVAS = (500, 500)
    FRAMES = 21
        
    box_size = (20, 20)
    box_depth = (-10, 8)
            
    rows = 21
    columns = 21
    layers = 1

    alpha = 1
   
    scale = 1

    block_width = (box_size[0] * columns + math.fabs(box_depth[0]) * layers) * scale
    block_height = (box_size[1] * rows + math.fabs(box_depth[1]) * layers) * scale

    canvas_center = (CANVAS[0]/2, CANVAS[1]/2)
    loc = (canvas_center[0] + block_width / 2 - (box_size[0] + (layers - 1) * math.fabs(box_depth[0])) * scale, canvas_center[1] - block_height / 2 + ((layers - 1) * math.fabs(box_depth[1])) * scale)

    box = make_box(box_size, box_depth)

    for frame in range(FRAMES):
        
        db.newPage(*CANVAS)
        frameDuration(1/FRAMES)
    
        db.fill(0)
        db.rect(0, 0, CANVAS[0], CANVAS[1])
    
        db.translate(*loc)
        db.scale(scale)
     
        db.fill(0)
        db.stroke(1)
        db.strokeWidth(2)
        db.lineJoin('round')
  
        for row in range(rows):
            db.save()
            translate(math.sin(row + frame) * alpha, row * box_size[1] + (box_depth[0]/box_size[0]) * math.sin(row + frame) * alpha)
            db.drawPath(box)
            for column in range(columns):
                db.save()
                translate(-column * box_size[0] + math.sin(column + frame) * alpha, (box_depth[0]/box_size[0]) * math.sin(column + frame) * alpha)
                db.drawPath(box)
                db.restore()
            db.restore()

    sh.saveSketch('draw')
    
    db.endDrawing()