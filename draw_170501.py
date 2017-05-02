# drawbot 170501

size(500, 500)

centX = width()/2
centY = height()/2

fps = 30

fill(180/255)
rect(0, 0, width(), height())

diam = 10

while diam <= 400:
    frameDuration(1/fps)

    newPage(width(), height())
    fill(180/255)
    rect(0, 0, width(), height())

    stroke(0)
    strokeWidth(5)
    fill(255/255, 50/255)

    oval(centX - diam/2, centY - diam/2, diam, diam)

    tempdiam = diam

    while tempdiam > 10:
        strokeWidth(1)
        fill(255/255, 25/255)
        oval(centX - tempdiam/2, centY - tempdiam/2, tempdiam, tempdiam)
        tempdiam -= 10

    diam += 10

saveImage("/Users/shu/Downloads/test.gif")