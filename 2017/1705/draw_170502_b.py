# drawbot 170502

size(500, 500)
a = 12

for x in xrange(a):
    for y in xrange(a):
        fill(x/a, y/a, 0.5)
        rect(x*30, y*30, y*a, x*a)

        