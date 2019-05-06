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
        self.tturn += self.tturninc
        self.diameter += self.incdiameter
        if self.diameter > self.maxdiameter:
            self.diameter = self.mindiameter
        if self.diameter < self.mindiameter:
            self.diameter = self.maxdiameter


class mytriangle():
    x1 = y1 = x2 = y2 = x3 = y3 = 0.0
    tturn = 0
    tsize = 250
    tturninc = 360 / 36
    xoffset = xoffset = 0
    x1cos = y1sin = x2cos = y2sin = x3cos = y3sin = 0.0

    def setOffsets (self, xoff, yoff):
        self.xoffset = xoff
        self.yoffset = yoff
        print ("Offset set to: (%d,%d)\n" % (self.xoffset, self.yoffset))
        
    def calculatevars (self, phi):
        self.x1cos = cos(math.radians(phi))
        self.y1sin = sin(math.radians(phi))
        phi = phi + 120
        self.x2cos = cos(math.radians(phi))
        self.y2sin = sin(math.radians(phi))
        phi = phi + 120
        self.x3cos = cos(math.radians(phi))
        self.y3sin = sin(math.radians(phi))

    def calculateFromAngle(self, diameter):
        self.x1 = self.x1cos * diameter + self.xoffset
        self.y1 = self.y1sin * diameter + self.yoffset
        self.x2 = self.x2cos * diameter + self.xoffset
        self.y2 = self.y2sin * diameter + self.yoffset
        self.x3 = self.x3cos * diameter + self.xoffset
        self.y3 = self.y3sin * diameter + self.yoffset

    def setTurnDegree(self, tphi):
        self.tturninc = tphi

    def drawTriangle(self):
        self.calculatevars(self.tturn)
        self.calculateFromAngle(self.tsize)
        triangle(self.x1,self.y1,self.x2,self.y2,self.x3,self.y3)
        self.drawEdges(self.tsize)
        self.tturn += self.tturninc
        
    def drawEdges(self, diameter):
        edgewith = diameter / 5
        nx1 = self.x1
        ny1 = self.y1
        nx2 = self.x2
        ny2 = self.y2
        nx3 = self.x3
        ny3 = self.y3
        if (nx2 - nx1) != 0:
            phi12 = atan2(nx2 - nx1,ny2 - ny1)
            px12 = nx2 - edgewith * sin(phi12)
            py12 = ny2 - edgewith * cos(phi12)
            phi13 = atan2(nx2 - nx3,ny2 - ny3)
            px13 = nx2 - edgewith * sin(phi13)
            py13 = ny2 - edgewith * cos(phi13)
            fill(255,0,0)
            triangle(nx2,ny2,px12,py12,px13,py13)
            noFill()
        else:
            # do the special case later
            pass
                
        if (nx3 - nx2) != 0:
            phi23 = atan2(nx3 - nx2,ny3 - ny2)
            px23 = nx3 - edgewith * sin(phi23)
            py23 = ny3 - edgewith * cos(phi23)
            phi21 = atan2(nx3 - nx1,ny3 - ny1)
            px21 = nx3 - edgewith * sin(phi21)
            py21 = ny3 - edgewith * cos(phi21)
            fill(255,0,0)
            triangle(nx3,ny3,px23,py23,px21,py21)
            noFill()
        else:
            pass
        if (nx1 - nx3) != 0:
            phi31 = atan2(nx1 - nx3,ny1 - ny3)
            px31 = nx1 - edgewith * sin(phi31)
            py31 = ny1 - edgewith * cos(phi31)
            phi32 = atan2(nx1 - nx2,ny1 - ny2)
            px32 = nx1 - edgewith * sin(phi32)
            py32 = ny1 - edgewith * cos(phi32)
            fill(255,0,0)
            triangle(nx1,ny1,px31,py31,px32,py32)
            noFill()
        else:
            pass
            

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
    circ.setMinDiameter(100)
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
    
