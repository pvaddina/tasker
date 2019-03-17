import operator
import math
from enum import Enum

class Orientation(Enum):
    INTERSECTING = 1
    ORTHOGONAL = 2
    PARALLEL = 3
    PARALLEL_AND_SAME = 4
    ORTHOGONAL_AND_PARALLEL = 5


#### A vector class
#### Note that the coordinates represent the maginitude and the direction of change
#### They are not really points
class Vector(object):
    def __init__(self, liCoordinates):
        if liCoordinates:
            try:
                self.mDimension = len(liCoordinates)
                assert(self.mDimension >= 2)
                self.mCoordinates = list(liCoordinates)
            except AssertionError:
                raise Exception("A vector can be formed with atleast two coordinates")
        else:
            self.mDimension = 0
            self.mCoordinates = []

    # Make a Vector joining two points. Note the two input arguments represent two points.
    def MakeVectorFromPoints(self, liPoint1, liPoint2):
        if (len(liPoint1) == len(liPoint2)):
            self.mCoordinates = [val-liPoint1[idx] for idx,val in enumerate(liPoint2)]
            self.mDimension = len(self.mCoordinates)

    def __str__(self):
        return "Vector coordinates: {}".format(self.mCoordinates)

    def __eq__(self, v):
        return self.mCoordinates == v.mCoordinates

    def __add__(self, v):
        return Vector(list(map(operator.add, self.mCoordinates, v.mCoordinates)))

    def __sub__(self, v):
        return Vector(list(map(operator.sub, self.mCoordinates, v.mCoordinates)))

    def __mul__(self, v):
        if type(v)==int or type(v)==float:
            return Vector([v*i for i in self.mCoordinates])
        else:
            raise TypeError("Unsupported operand types")

    def Magnitude(self):
        sq = [i*i for i in self.mCoordinates]
        return math.sqrt(sum(sq))

    def Normalize(self):
        mag = self.Magnitude()
        if mag > 0:
            self.mCoordinates = [i/mag for i in self.mCoordinates]

    def DotProduct(self,v):
        l = len(self.mCoordinates)
        p = 0
        for i in range(0,l):
            p += self.mCoordinates[i]*v.mCoordinates[i]
        return round(p, 3)

    def CrossProduct(self,v):
        #assert(len(self.mCoordinates) == 3 and len(v.mCoordinates) == 3)
        if(len(self.mCoordinates) == 3 and len(v.mCoordinates) == 3):
            coord = lambda x,y: round(x[0]*y[1] - x[1]*y[0], 3)
            gen = lambda x,ignoreIdx: [item for idx,item in enumerate(x) if idx != ignoreIdx]
            return [coord(gen(self.mCoordinates,0), gen(v.mCoordinates,0))
                ,-coord(gen(self.mCoordinates,1), gen(v.mCoordinates,1))
                ,coord(gen(self.mCoordinates,2), gen(v.mCoordinates,2))]
        elif (len(self.mCoordinates) == 2 and len(v.mCoordinates) == 2):
            self.mCoordinates.append(0)
            v.mCoordinates.append(0)
            self.CrossProduct(v)
        else:
            raise ValueError("Need 2 or 3 coordinate vectors")

    def ParallelogramArea(self, v):
        cpVector = Vector(self.CrossProduct(v))
        return cpVector.Magnitude()

    def TriangleArea(self, v):
        return self.ParallelogramArea(v)/2

    def AngleRad(self,v):
        lhs = self.DotProduct(v)
        rhs_mag = self.Magnitude() * v.Magnitude()
        res = lhs/rhs_mag
        return math.acos(round(res,3))

    def AngleDeg(self,v):
        rad = self.AngleRad(v)
        deg = round(math.degrees(rad),3)
        return deg

    def IsZeroVector(self):
        return self.Magnitude() == 0

    def GetOrientation(self,v):
        p = Orientation.INTERSECTING

        if self.DotProduct(v) == 0:
            p = Orientation.ORTHOGONAL

        isParallel = (v.IsZeroVector()
                     or self.IsZeroVector()
                     or self.AngleDeg(v) == 0
                     or self.AngleDeg(v) == 180)

        if isParallel:
            if p == Orientation.ORTHOGONAL:
                p = Orientation.ORTHOGONAL_AND_PARALLEL
            else:
                p = Orientation.PARALLEL
        
        return p


