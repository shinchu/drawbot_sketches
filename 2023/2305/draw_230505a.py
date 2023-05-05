import sys
import os
from perlin_noise import PerlinNoise
from math import sin, tau

SIZE = 500
N = 100
FPS = 15
DURATION = 1 / FPS
SECONDS = 3
TOTALFRAMES = SECONDS * FPS

noise = PerlinNoise()

for frame in range(TOTALFRAMES):
    newPage(SIZE, SIZE)
    frameDuration(DURATION)
    stroke(None)
    fill(0.8)
    rect(0, 0, SIZE, SIZE)
    fill(1)

    for i in range(N + 1):
        for j in range(N + 1):
            osize = 1.3 * SIZE / N * sin(frame * 0.02 + i * j * 0.01 + tau * noise([i * 0.3, j * 0.3, frame * 0.03]))
            oval(SIZE/N * i, SIZE/N * j, osize, osize)

# Save image
save_dir = os.path.expanduser('~/Downloads')
file_name = 'noise.gif'
saveImage(os.path.join(save_dir, file_name), imageResolution=144)