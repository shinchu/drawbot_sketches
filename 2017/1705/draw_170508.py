# drawbot 170508

from sketch_helper import saveSketch

canvas = 500
fps = 50

for angle1 in range(45, 91 + 45, 1):

    newPage(canvas, canvas)
    frameDuration(1/fps)
    
    fill(1)
    rect(0, 0, width(), height())

    radius = 80
    thick = 50

    centx = (width() - thick)/2
    centy = (height() - thick)/2

    stroke(0)
    strokeWidth(3)
    
    angle2 = angle1 - 90
    angle3 = angle1 + 90
    angle4 = angle1 + 180

    x11 = centx + sin(radians(angle2)) * radius
    y11 = centy + cos(radians(angle2)) * radius
    x12 = centx + sin(radians(angle1)) * radius
    y12 = centy + cos(radians(angle1)) * radius
    x13 = centx + sin(radians(angle3)) * radius
    y13 = centy + cos(radians(angle3)) * radius
    x14 = centx + sin(radians(angle4)) * radius
    y14 = centy + cos(radians(angle4)) * radius

    x21 = centx + thick + sin(radians(angle2)) * radius
    y21 = centy + thick + cos(radians(angle2)) * radius
    x22 = centx + thick + sin(radians(angle1)) * radius
    y22 = centy + thick + cos(radians(angle1)) * radius
    x23 = centx + thick + sin(radians(angle3)) * radius
    y23 = centy + thick + cos(radians(angle3)) * radius
    x24 = centx + thick + sin(radians(angle4)) * radius
    y24 = centy + thick + cos(radians(angle4)) * radius

    if angle1 < 90:

        line((x11, y11), (x12, y12))
        line((x12, y12), (x13, y13))
        line((x13, y13), (x14, y14))
        line((x14, y14), (x11, y11))

        line((x11, y11), (x21, y21))
        line((x12, y12), (x22, y22))
        line((x13, y13), (x23, y23))

        line((x21, y21), (x22, y22))
        line((x22, y22), (x23, y23))
    
    else:
        
        line((x11, y11), (x12, y12))
        line((x12, y12), (x13, y13))
        line((x13, y13), (x14, y14))
        line((x14, y14), (x11, y11))

        line((x11, y11), (x21, y21))
        line((x12, y12), (x22, y22))
        line((x14, y14), (x24, y24))

        line((x21, y21), (x22, y22))
        line((x21, y21), (x24, y24))

saveSketch("draw")
