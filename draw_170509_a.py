# drawbot 170509

from sketch_helper import saveSketch

canvas = 500
fps = 50

for angle1 in range(0, 91, 1):

    newPage(canvas, canvas)
    frameDuration(1/fps)
    
    fill(1)
    rect(0, 0, width(), height())

    ry = 50
    rx = 100
    thick = 120

    centx = width()/2
    centy = (height() + thick)/2

    angle2 = 90 + angle1
    angle3 = 180 + angle1
    angle4 = 270 + angle1

    x11 = centx + cos(radians(angle1)) * rx
    y11 = centy + sin(radians(angle1)) * ry
    x12 = centx + cos(radians(angle2)) * rx
    y12 = centy + sin(radians(angle2)) * ry
    x13 = centx + cos(radians(angle3)) * rx
    y13 = centy + sin(radians(angle3)) * ry
    x14 = centx + cos(radians(angle4)) * rx
    y14 = centy + sin(radians(angle4)) * ry

    x21 = centx + cos(radians(angle1)) * rx
    y21 = centy - thick + sin(radians(angle1)) * ry
    x22 = centx + cos(radians(angle2)) * rx
    y22 = centy - thick + sin(radians(angle2)) * ry
    x23 = centx + cos(radians(angle3)) * rx
    y23 = centy - thick + sin(radians(angle3)) * ry
    x24 = centx  + cos(radians(angle4)) * rx
    y24 = centy - thick + sin(radians(angle4)) * ry

    stroke(0)
    strokeWidth(3)

    if angle1 < 45:

        line((x11, y11), (x12, y12))
        line((x12, y12), (x13, y13))
        line((x13, y13), (x14, y14))
        line((x11, y11), (x14, y14))

        line((x23, y23), (x24, y24))
        line((x21, y21), (x24, y24))

        line((x11, y11), (x21, y21))
        line((x13, y13), (x23, y23))
        line((x14, y14), (x24, y24))
    
    else:
        
        line((x11, y11), (x12, y12))
        line((x12, y12), (x13, y13))
        line((x13, y13), (x14, y14))
        line((x11, y11), (x14, y14))
        
        line((x23, y23), (x24, y24))
        line((x22, y22), (x23, y23))
        
        line((x12, y12), (x22, y22))
        line((x13, y13), (x23, y23))
        line((x14, y14), (x24, y24))

saveSketch("draw")
