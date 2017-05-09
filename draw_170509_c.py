# drawbot 170509

from sketch_helper import saveSketch

def cubeRotateH(centx, centy, radius, thick, angle1):
    
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
        
def cubeRotateV1(centx, centy, rx, ry, thick, angle1):
    
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

def cubeRotateV2(centx, centy, rx, ry, thick, angle1):
    
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

    x21 = centx - thick +  cos(radians(angle1)) * rx
    y21 = centy + sin(radians(angle1)) * ry
    x22 = centx - thick + cos(radians(angle2)) * rx
    y22 = centy + sin(radians(angle2)) * ry
    x23 = centx - thick + cos(radians(angle3)) * rx
    y23 = centy + sin(radians(angle3)) * ry
    x24 = centx - thick + cos(radians(angle4)) * rx
    y24 = centy + sin(radians(angle4)) * ry

    if angle1 < 45:

        line((x11, y11), (x12, y12))
        line((x12, y12), (x13, y13))
        line((x13, y13), (x14, y14))
        line((x11, y11), (x14, y14))

        line((x22, y22), (x23, y23))
        line((x23, y23), (x24, y24))

        line((x12, y12), (x22, y22))
        line((x13, y13), (x23, y23))
        line((x14, y14), (x24, y24))
    
    else:
        
        line((x11, y11), (x12, y12))
        line((x12, y12), (x13, y13))
        line((x13, y13), (x14, y14))
        line((x11, y11), (x14, y14))
        
        line((x21, y21), (x22, y22))
        line((x22, y22), (x23, y23))
        
        line((x11, y11), (x21, y21))
        line((x12, y12), (x22, y22))
        line((x13, y13), (x23, y23))


canvas = 500
fps = 50

for angle in range(0, 91, 1):

    newPage(canvas, canvas)
    frameDuration(1/fps)

    fill(0)
    rect(0, 0, width(), height())

    stroke(1)
    strokeWidth(2)

    cubeRotateV1(width()/6, height()*2/3 + height()/6 + 30, 50, 25, 60, angle)
    cubeRotateV2(width()/3 + width()/6 + 30, height()*2/3 + height()/6, 25, 50, 60, angle)
    cubeRotateH(width()*2/3 + width()/6-15, height()*2/3 + height()/6 -15, 48, 30, angle + 45)

    cubeRotateH(width()/6-15, height()/2-15, 48, 30, angle + 45)
    cubeRotateV1(width()/3 + width()/6, height()/2 + 30, 50, 25, 60, angle)
    cubeRotateV2(width()*2/3 + width()/6 + 30, height()/2, 25, 50, 60, angle)

    cubeRotateV2(width()/6 + 30, height()/6, 25, 50, 60, angle)
    cubeRotateH(width()/3 + width()/6-15, height()/6-15, 48, 30, angle + 45)
    cubeRotateV1(width()*2/3 + width()/6, height()/6 + 30, 50, 25, 60, angle)
        
saveSketch("draw")