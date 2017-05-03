# Generate a jellyfish-like pulsating blobby animation.

from random import seed
from fontTools.pens.basePen import BasePen

# Define this so we can use TrueType-style quadratic curves. Ideal for blobbies!
class BezierPathPen(BasePen):
    """FontTools pen -> BezierPath adapter."""
    def __init__(self, glyphSet, bezPath):
        super(BezierPathPen, self).__init__(glyphSet)
        self.bezPath = bezPath
    def _moveTo(self, pt):
        self.bezPath.moveTo(pt)
    def _lineTo(self, pt):
        self.bezPath.lineTo(pt)
    def _curveToOne(self, pt1, pt2, pt3):
        self.bezPath.curveTo(pt1, pt2, pt3)
    def _closePath(self):
        self.bezPath.closePath()

def varyPoint(pt, radius, phase):
    x, y = pt
    dx = radius * cos(phase)
    dy = radius * sin(phase)
    return x + dx, y + dy

def drawBlob(blobPhase, blobRadius):
    points = []  # list of off curve points forming the blob.
    for i in range(numBlobPoints):
        a = 2 * pi * i / numBlobPoints
        x = blobRadius * cos(a)
        y = blobRadius * sin(a)
        rPhase, rSign = randomPhases[i]
        points.append(varyPoint((x, y), 0.2 * blobRadius, rPhase + rSign * 2 * pi * blobPhase))
    # Add a final 'fake' point, to tell the pen there is *no* on curve point at all
    points.append(None)
    bezPath = BezierPath()
    p = BezierPathPen(None, bezPath)
    p.qCurveTo(*points)
    p.closePath()
    drawPath(bezPath)

seed(0)  # Ok ok, make this animation predictable.
numBlobPoints = 5
randomPhases = [(2 * pi * random(), choice([-1, 1])) for i in range(numBlobPoints)]

canvasSize = 500
nBlobs = 20
nFrames = 95

for frame in range(nFrames):
    framePhase = frame / nFrames
    newPage(canvasSize, canvasSize)
    frameDuration(1/20)
    fill(0)
    rect(0, 0, canvasSize, canvasSize)
    translate(canvasSize/2, canvasSize/2)
    strokeWidth(2)
    stroke(1)
    fill(1)
    for i in range(nBlobs):
        blobPhase = i / nBlobs
        radius = 5 + i * 5
        drawBlob(framePhase + blobPhase * 0.75, radius)

saveImage("/Users/shu/Downloads/test.gif")