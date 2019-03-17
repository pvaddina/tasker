import inspect
import vector as vec

class Plane(object):
    def __init__(self, liCoordinates, constant):
        assert(len(liCoordinates) == 3)
        self.mNormalVector = vec.Vector(liCoordinates)
        self.mK = constant
        self.mDimension = len(liCoordinates)
        self.mBasepoints = []
        if liCoordinates[0] != 0:
            self.mBasepoints.append([constant/liCoordinates[0], 0, 0])
        elif liCoordinates[1] != 0:
            self.mBasepoints.append([0, constant/liCoordinates[1], 0])
        elif liCoordinates[2] != 0:
            self.mBasepoints.append([0, 0, constant/liCoordinates[2]])

    def __str__(self):
        return "Normal vector of the Plane: {}".format(self.mNormalVector)

    def __add__(self, p):
        try:
            assert(isinstance(p, Plane))
            return Plane((self.mNormalVector + p.mNormalVector).mCoordinates, self.mK+p.mK)
        except AssertionError:
            raise Exception("Addition operation only possible on a Plane type")

    def __mul__(self, val):
        return Plane([x*val for x in self.mNormalVector.mCoordinates], self.mK*val)

    def GetNonZeroCoefficients(self):
        nzCoordIdxs = [idx for idx,value in enumerate(self.mNormalVector.mCoordinates) if value != 0 ]
        return len(nzCoordIdxs), nzCoordIdxs

    def InsertAndSolve(self, index, value):
        self.mK = self.mK - (self.mNormalVector.mCoordinates[index]*value)
        self.mNormalVector.mCoordinates[index] = 0

    def ArePlanesParallel(self,inPlane):
        return self.mNormalVector.GetOrientation(inPlane.mNormalVector) == vec.Orientation.PARALLEL

    def ArePlanesEqual(self,inPlane):
        if self.mBasepoints and inPlane.mBasepoints:
            vecJoiningTwoPlanes = vec.Vector([])
            vecJoiningTwoPlanes.MakeVectorFromPoints(self.mBasepoints[0], inPlane.mBasepoints[0])
            return (vecJoiningTwoPlanes.GetOrientation(self.mNormalVector) == vec.Orientation.ORTHOGONAL) and (vecJoiningTwoPlanes.GetOrientation(inPlane.mNormalVector) == vec.Orientation.ORTHOGONAL)
        return False

    def NormalizeCoefficient(self,idx):
        denom = self.mNormalVector.mCoordinates[idx]
        if denom:
            tempCoord = [x/denom for x in self.mNormalVector.mCoordinates]
            self.mNormalVector = vec.Vector(tempCoord)
            self.mK = self.mK/denom

    def GetIntersection(self,inPlane):
        if self.ArePlanesEqual(inPlane):
            return vec.Orientation.PARALLEL_AND_SAME,[]
        elif self.ArePlanesParallel(inPlane):
            return vec.Orientation.PARALLEL,[]
        else:
            return vec.Orientation.INTERSECTING, []



