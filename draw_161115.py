# drawbot 161115

from sketch_helper import *

CANVAS = 500
SIZE = 25
NUMBERS = 16

size(CANVAS, CANVAS)

pen = BezierPath()

pen.moveTo((543, 264))
pen.curveTo((569, 273), (610, 279), (649, 279))
pen.curveTo((697, 278), (745, 262), (775, 242))
pen.curveTo((801, 225), (820, 204), (820, 190))
pen.curveTo((820, 183), (816, 177), (806, 172))
pen.curveTo((780, 160), (750, 151), (721, 143))
pen.curveTo((709, 140), (705, 133), (705, 129))
pen.curveTo((705, 123), (710, 120), (722, 121))
pen.curveTo((758, 123), (786, 126), (809, 125))
pen.curveTo((832, 125), (844, 121), (853, 115))
pen.curveTo((859, 111), (868, 106), (881, 106))
pen.curveTo((898, 106), (916, 122), (916, 149))
pen.curveTo((916, 191), (891, 226), (856, 253))
pen.curveTo((803, 299), (734, 312), (664, 312))
pen.curveTo((623, 312), (573, 306), (523, 290))
pen.curveTo((449, 381), (425, 416), (425, 454))
pen.curveTo((425, 511), (505, 562), (543, 562))
pen.curveTo((557, 562), (571, 556), (588, 556))
pen.curveTo((607, 556), (617, 567), (617, 584))
pen.curveTo((617, 606), (603, 624), (584, 637))
pen.curveTo((561, 653), (546, 660), (517, 669))
pen.curveTo((439, 693), (419, 715), (405, 758))
pen.curveTo((402, 768), (398, 773), (393, 773))
pen.curveTo((386, 773), (382, 768), (382, 756))
pen.curveTo((382, 732), (387, 710), (398, 693))
pen.curveTo((417, 662), (451, 630), (493, 606))
pen.curveTo((415, 530), (390, 487), (390, 434))
pen.curveTo((390, 404), (397, 381), (414, 353))
pen.curveTo((429, 327), (448, 301), (471, 270))
pen.curveTo((417, 245), (361, 216), (312, 188))
pen.curveTo((268, 162), (226, 137), (200, 121))
pen.curveTo((173, 104), (154, 95), (141, 95))
pen.curveTo((128, 95), (119, 104), (112, 112))
pen.curveTo((102, 124), (98, 130), (93, 142))
pen.curveTo((92, 145), (88, 147), (85, 147))
pen.curveTo((82, 147), (76, 142), (75, 137))
pen.curveTo((72, 126), (72, 117), (72, 105))
pen.curveTo((72, 88), (84, 66), (102, 43))
pen.curveTo((119, 22), (141, 7), (160, 7))
pen.curveTo((175, 7), (185, 16), (193, 31))
pen.curveTo((220, 58), (243, 77), (274, 102))
pen.curveTo((337, 76), (379, 58), (407, 45))
pen.curveTo((435, 33), (446, 25), (458, 16))
pen.curveTo((468, 8), (480, 5), (495, 5))
pen.curveTo((551, 5), (612, 47), (612, 122))
pen.curveTo((612, 164), (590, 204), (543, 264))
pen.closePath()
pen.moveTo((490, 244))
pen.curveTo((520, 202), (539, 163), (539, 127))
pen.curveTo((539, 96), (519, 78), (490, 78))
pen.curveTo((464, 78), (435, 81), (407, 86))
pen.curveTo((378, 92), (339, 102), (296, 119))
pen.curveTo((354, 169), (426, 215), (490, 244))
pen.closePath()
pen.moveTo((806, 753))
pen.curveTo((756, 753), (715, 712), (715, 662))
pen.curveTo((715, 612), (756, 571), (806, 571))
pen.curveTo((856, 571), (897, 612), (897, 662))
pen.curveTo((897, 712), (856, 753), (806, 753))
pen.closePath()
pen.moveTo((806, 721))
pen.curveTo((839, 721), (865, 695), (865, 662))
pen.curveTo((865, 629), (839, 603), (806, 603))
pen.curveTo((773, 603), (747, 629), (747, 662))
pen.curveTo((747, 695), (773, 721), (806, 721))
pen.closePath()

stroke(0.3)
fill(0.9)
drawGrid(CANVAS, CANVAS, SIZE, NUMBERS)

translate(0, (CANVAS - SIZE * NUMBERS) / 2)
fill(0.7)
stroke(0.2)
strokeWidth(1)
pen.scale(1/2)
drawPath(pen)

stroke(0.3)
strokeWidth(0.7)
drawHandle(pen, 3)

saveSketch("draw")