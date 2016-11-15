from robofab.world import RFont
from sketch_helper import *
from robofab.pens.pointPen import *

ufo = u"/users/shu/Dropbox/UT/Research/research_scripts/lis_font_ufo/lis_acorn.ufo"

font = RFont(ufo)
glyph = font['uni304E']

w = 500
h = 500
sc = 550

UPM = font.info.unitsPerEm
xmin, ymin, xmax, ymax = glyph.box
glyph_x = xmin + (xmax - xmin)/2
glyph_y = ymin + (ymax - ymin)/2

for contour in glyph:
    print contour.clockwise
    if contour.clockwise is True:
        print contour.box
        xmin, ymin, xmax, ymax = contour.box
        x = xmin + (xmax - xmin)/2
        y = ymin + (ymax - ymin)/2
        if y < glyph_y:
            if y > 0:
                contour.scale((0.8, 0.5), center=(x, y * 1.2))
            else:
                contour.scale((0.9, 0.5), center=(x, y * 0.5))


glyph.update()

size(w, h)
B = BezierPath()
for contour in glyph:
    for i, segment in enumerate(contour):
        # curveTo
        if len(segment.points) == 3:
            x1, y1 = segment.points[0].x, segment.points[0].y
            x2, y2 = segment.points[1].x, segment.points[1].y
            x3, y3 = segment.points[2].x, segment.points[2].y
            B.curveTo((x1, y1), (x2, y2), (x3, y3))
        # lineTo or moveTo
        else:
            x, y = segment.points[0].x, segment.points[0].y
            if i == 0:
                B.moveTo((x, y))
            else:
                B.lineTo((x, y))

translate(0, 0)
B.scale(sc/UPM)
drawPath(B)