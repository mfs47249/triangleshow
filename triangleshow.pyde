import math
import copy

class mycircle():
    diameter = 100.0
    mindiameter = diameter
    maxdiameter = diameter * 10
    incdiameter = 10
    xoffset = 0
    yoffset = 0


    def setOffsets (self, xoff, yoff):
        self.xoffset = xoff
        self.yoffset = yoff

    def setDiameter(self, dia):
        self.diameter = dia

    def setIncDiameter(self, incvalue):
        self.incdiameter = incvalue

    def setMinDiameter(self, minvalue):
        self.mindiameter = minvalue

    def setMaxDiameter(self, maxvalue):
        self.maxdiameter = maxvalue

    def drawcircle(self):
        ellipse(self.xoffset, self.yoffset, self.diameter, self.diameter)
        self.diameter += self.incdiameter
        if self.diameter > self.maxdiameter:
            self.diameter = self.mindiameter
        if self.diameter < self.mindiameter:
            self.diameter = self.maxdiameter

class mycirclesegments():
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    x3 = 0.0
    y3 = 0.0
    tturn = 0
    tsize = 250
    tturninc = -360 / 36
    diameter = 400.0
    mindiameter = diameter
    maxdiameter = diameter * 10
    incdiameter = 0
    xoffset = 0
    yoffset = 0


    def calculateFromAngle(self, phi, diameter):
        self.x1 = sin(math.radians(phi)) * diameter + self.xoffset
        self.y1 = cos(math.radians(phi)) * diameter + self.yoffset
        phi = phi + 120
        self.x2 = sin(math.radians(phi)) * diameter + self.xoffset
        self.y2 = cos(math.radians(phi)) * diameter + self.yoffset
        phi = phi + 120
        self.x3 = sin(math.radians(phi)) * diameter + self.xoffset
        self.y3 = cos(math.radians(phi)) * diameter + self.yoffset

    def setOffsets (self, xoff, yoff):
        self.xoffset = xoff
        self.yoffset = yoff

    def setDiameter(self, dia):
        self.diameter = dia

    def setIncDiameter(self, incvalue):
        self.incdiameter = incvalue

    def setMinDiameter(self, minvalue):
        self.mindiameter = minvalue

    def setMaxDiameter(self, maxvalue):
        self.maxdiameter = maxvalue

    def setTurnDegree(self, tphi):
        self.tturninc = tphi

    def drawsegments(self):
        self.calculateFromAngle(self.tturn, self.tsize)
        arc(self.xoffset, self.yoffset, self.diameter, self.diameter, radians(self.tturn + 40), radians(self.tturn + 80))
        arc(self.xoffset, self.yoffset, self.diameter, self.diameter, radians(self.tturn + 160), radians(self.tturn + 200))
        arc(self.xoffset, self.yoffset, self.diameter, self.diameter, radians(self.tturn + 280), radians(self.tturn + 320))
        self.tturn -= self.tturninc
        self.diameter += self.incdiameter
        if self.diameter > self.maxdiameter:
            self.diameter = self.mindiameter
        if self.diameter < self.mindiameter:
            self.diameter = self.maxdiameter


class mytriangle():
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0
    x3 = 0.0
    y3 = 0.0
    tturn = 0
    tsize = 250
    tturninc = 360 / 36
    xoffset = 0
    xoffset = 0

    def setOffsets (self, xoff, yoff):
        self.xoffset = xoff
        self.yoffset = yoff
        print ("Offset set to: (%d,%d)\n" % (self.xoffset, self.yoffset))

    def calculateFromAngle(self, phi, diameter):
        self.x1 = cos(math.radians(phi)) * diameter + self.xoffset
        self.y1 = sin(math.radians(phi)) * diameter + self.yoffset
        phi = phi + 120
        self.x2 = cos(math.radians(phi)) * diameter + self.xoffset
        self.y2 = sin(math.radians(phi)) * diameter + self.yoffset
        phi = phi + 120
        self.x3 = cos(math.radians(phi)) * diameter + self.xoffset
        self.y3 = sin(math.radians(phi)) * diameter + self.yoffset

    def setTurnDegree(self, tphi):
        self.tturninc = tphi

    def drawTriangle(self):
        self.calculateFromAngle(self.tturn, self.tsize)
        triangle(self.x1,self.y1,self.x2,self.y2,self.x3,self.y3)
        self.tturn -= self.tturninc


def setup():
    global tria, circ, circ1, circ2, segments, ball

    size (800,800)
    tria = mytriangle()
    tria.setOffsets(400,400)
    tria.setTurnDegree(1)

    segments = mycirclesegments()
    segments.setOffsets(400,400)
    segments.setTurnDegree(1)

    circ = mycircle()
    circ.setOffsets(400,400)
    circ.setMaxDiameter(1200)
    circ.setMinDiameter(50)
    circ.setIncDiameter(10)
    circ.setDiameter(400)

    ball = copy.deepcopy(circ)
    ball.setMinDiameter(10)
    ball.setMaxDiameter(50)
    ball.setIncDiameter(-1)

    noFill()
    frameRate(25)
    stroke(255,0,0)
    strokeWeight(5)
    strokeCap(ROUND)


def draw():
    global counter, millitime
    millitime = millis()
    background(0)
    noFill()
    stroke(128,128,128)
    tria.drawTriangle()
    stroke(255,0,0)
    circ.drawcircle()
    segments.drawsegments()
    fill(255,0,0)
    ball.drawcircle()
    outstring = "Number:%d Milliseconds:%d" % (counter, millis() - millitime)
    print (outstring)
    counter += 1

if __name__ == "__main__":
    print ("main startet")
    counter = 0
    millitime = 0
    
