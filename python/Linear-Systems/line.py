import vector as vec

# A class representing a Line Equation composed of two points
class Line(object):
    def __init__(self, liCoordinates, constant):
        try:
            assert(len(liCoordinates) == 2)
            self.mNormalVector = vec.Vector(liCoordinates)
            self.mK = constant
            self.mBasepoints = []
            if liCoordinates[0] != 0:
                self.mBasepoints.append([constant/liCoordinates[0], 0])
            elif liCoordinates[1] != 0:
                self.mBasepoints.append([0, constant/liCoordinates[1]])
        except AssertionError:
            raise Exception("A line object can be created with two coordinates only (equation of the form, Ax+By=k)")

    def __str__(self):
        return "Line: {}".format(self.mNormalVector)

    # Check if two lines are parallel. They are parallel when the Normal 
    # vectors of the two are parallel to each other
    def AreLinesParallel(self,inLine):
        return self.mNormalVector.GetOrientation(inLine.mNormalVector) == vec.Orientation.PARALLEL

    # Check if two lines are equal 
    def AreLinesEqual(self,inLine):
        if self.AreLinesParallel(inLine):
            cDimensions = self.mNormalVector.mDimension
            n1 = len(self.mBasepoints)
            n2 = len(inLine.mBasepoints)
            if cDimensions == inLine.mNormalVector.mDimension:
                if n1 == n2:
                    if n1 == cDimensions:
                        vecJoiningTwoLines = vec.Vector([])
                        vecJoiningTwoLines.MakeVectorFromPoints(self.mBasepoints[0], inLine.mBasepoints[1])
                        return (vecJoiningTwoLines.GetOrientation(self.mNormalVector) == vec.Orientation.ORTHOGONAL) and (vecJoiningTwoLines.GetOrientation(inLine.mNormalVector) == vec.Orientation.ORTHOGONAL)
                    else:
                        return self.mBasepoints[0] == inLine.mBasepoints[0]
        return False


    def GetIntersection(self,inLine):
        if self.AreLinesEqual(inLine):
            return vec.Orientation.PARALLEL_AND_SAME,[]
        elif self.AreLinesParallel(inLine):
            return vec.Orientation.PARALLEL,[]
        else:
            A,B=self.mNormalVector.mCoordinates
            k1 = self.mK
            C,D=inLine.mNormalVector.mCoordinates
            k2 = inLine.mK
            denominator = A*D-B*C
            return vec.Orientation.INTERSECTING, [(D*k1-B*k2)/denominator, (A*k2-C*k1)/denominator]



