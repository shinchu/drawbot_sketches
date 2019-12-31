# drawbot 170503

canvas = 500
oheight = 300
owidth = 280
ioheight = 0.6*oheight
iowidth = 0.5*owidth

size(500, 500)
fill(1)
rect(0, 0, width(), height())

fill(0.6)
oval((width()-owidth)/2, (height()-oheight)/2, owidth, oheight)

fill(1)
oval((width()-iowidth)/2, (height()-ioheight)/2, iowidth, ioheight)