#! /usr/bin/env python
# coding: utf-8
# draw_181227_a.py
# 2018-12-27
#
import os
import sys
import math
import random
sys.path.append(os.path.dirname(os.getcwd()))

import drawBot as db
import sketch_helper as sh

CANVAS = (1181, 1748)
# CANVAS = (1748, 1181)
SCALE = 0.3
MARGIN = 20

ufo_path = '/Users/shu/Dropbox/Life/Misc/nenga_2019/pig_2018.ufo'

if __name__ == "__main__":

    db.newDrawing()

    db.size(*CANVAS)

    glyphs = ['A', 'A', 'B', 'C', 'D', 'E', 'F']

    pig_outline = sh.getGlyphPath(ufo_path, 'A')
    min_x, min_y, max_x, max_y = pig_outline.bounds()
    width = (max_x - min_x)
    height = (max_y - min_y)

    vertical_pigs = math.floor(CANVAS[1] / ((height + MARGIN / 2) * SCALE))
    horizontal_pigs = math.floor(CANVAS[0] / ((width + MARGIN) * SCALE))

    # bottom_margin = (CANVAS[1] - vertical_pigs * ((height + MARGIN / 2) * SCALE)) / 2

    db.save()
    db.scale(SCALE)
    # db.rotate(45)
    # db.translate(CANVAS[0] * 0.8, -CANVAS[1] * 2.5)
    y = - 2 * height
    for i in range(vertical_pigs + 10):
        x = - 6 * width
        y += height + MARGIN / 2
        for j in range(horizontal_pigs + 30):
            x += width + MARGIN
            db.save()
            if i % 2 == 0:
                db.translate(x - 0.3 * width, y)
            else:
                db.translate(x + 0.3 * width, y)
            pig = sh.getGlyphPath(ufo_path, random.choice(glyphs))
            db.fill(j / 15, i / 20, 0.7, 1)
            db.drawPath(pig)
            db.restore()

    db.restore()

    db.save()
    db.translate(-160, -400)
    db.scale(2.5)
    # db.stroke(0, 0, 0, 1)
    db.stroke(0.8, 0.8, 0.8, 1)
    db.fill(1, 1, 1, 1)
    db.strokeWidth(20)
    db.lineJoin('round')
    db.drawPath(sh.getGlyphPath(ufo_path, 'I'))
    # db.stroke(0.95, 0.95, 0.95, 1)
    db.drawPath(sh.getGlyphPath(ufo_path, 'J'))
    db.fill(0.8, 0.8, 0.8, 1)
    db.stroke(None)
    db.drawPath(sh.getGlyphPath(ufo_path, 'K'))
    db.restore()

    db.save()
    db.translate(-160, 1400)
    db.scale(2.5)
    # db.stroke(0, 0, 0, 1)
    db.stroke(0.8, 0.8, 0.8, 1)
    db.fill(1, 1, 1, 1)
    db.strokeWidth(20)
    db.lineJoin('round')
    db.drawPath(sh.getGlyphPath(ufo_path, 'I'))
    # db.stroke(0.95, 0.95, 0.95, 1)
    db.drawPath(sh.getGlyphPath(ufo_path, 'J'))
    db.fill(0.8, 0.8, 0.8, 1)
    db.stroke(None)
    db.drawPath(sh.getGlyphPath(ufo_path, 'K'))
    db.drawPath(sh.getGlyphPath(ufo_path, 'L'))
    db.restore()

    db.save()
    db.font('Tsukushi B Round Gothic Bold', 200)
    db.fill(0.1)
    db.lineHeight(100)
    db.textBox('新謹春賀', (380, 100, 500, 1000))
    db.fontSize(46)
    db.lineHeight(30)
    # db.textBox('明けましておめでとうございます。', (240, 80, 800, 200))
    # db.textBox('本年も良い年でありますように、心よりお祈り申し上げます。', (240, -180, 700, 400))
    db.textBox('旧年中は大変お世話になりました。', (240, 80, 800, 200))
    db.textBox('皆様のご多幸とご健康をお祈りいたします。', (240, -180, 700, 400))
    db.restore()

    saveImage("/Users/shu/Downloads/pig.png", imageResolution = 300)

    db.endDrawing()
