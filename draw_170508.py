# drawbot 170508

canvas = 500

size(canvas, canvas)
fill(1)
rect(0, 0, width(), height())

radius = 100

move = 19
thick = 50


centx = (width() - thick)/2
centy = (height() - thick)/2

angle1 = 45
angle2 = 180 - angle1


stroke(0)
strokeWidth(3)

x11 = centx + move + sin(radians(-angle1)) * radius
y11 = centy + move + cos(radians(-angle1)) * radius
x12 = centx - move + sin(radians(angle1)) * radius
y12 = centy - move + cos(radians(angle1)) * radius
x13 = centx - move + sin(radians(angle2)) * radius
y13 = centy - move + cos(radians(angle2)) * radius
x14 = centx + move + sin(radians(-angle2)) * radius
y14 = centy + move + cos(radians(-angle2)) * radius

x21 = centx + move + thick + sin(radians(-angle1)) * radius
y21 = centy + move + thick + cos(radians(-angle1)) * radius
x22 = centx - move + thick + sin(radians(angle1)) * radius
y22 = centy - move + thick + cos(radians(angle1)) * radius
x23 = centx - move + thick + sin(radians(angle2)) * radius
y23 = centy - move + thick + cos(radians(angle2)) * radius
x24 = centx + move + thick + sin(radians(-angle2)) * radius
y24 = centy + move + thick + cos(radians(-angle2)) * radius

line((x11, y11), (x12, y12))
line((x12, y12), (x13, y13))
line((x13, y13), (x14, y14))
line((x14, y14), (x11, y11))

line((x11, y11), (x21, y21))
line((x12, y12), (x22, y22))
line((x13, y13), (x23, y23))

line((x21, y21), (x22, y22))
line((x22, y22), (x23, y23))
