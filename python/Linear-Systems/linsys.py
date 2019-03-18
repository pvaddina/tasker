import plane
import copy

class LinearSystem(object):
    def __init__(self, liPlanes):
        try:
            d = liPlanes[0].mDimension
            for p in liPlanes:
                assert d == p.mDimension            
            # Save the planes. But before that make sure the equations are sorted according to the
            # number of non-zero coefficients, in increasing order
            liPlanes = self.OrderPlanesInTriangForm(liPlanes)
            self.mLiPlanes = copy.deepcopy(liPlanes)
            self.mLiTempPlanes = copy.deepcopy(liPlanes)
            self.mSolutions = {}
        except AssertionError:
            raise Exception("All planes do not have the same Dimensions")

    def __len__(self):
        return len(self.mLiPlanes)

    def __str__(self):
        objectStr = ""
        for i in range(0,len(self.mLiPlanes)):
            objectStr += "Plane with Normal {}".format(self.mLiPlanes[i]) + "\n"
        solutionString = "The system has no solution"
        if self.mSolutions:
            solutionString = "Solution: {" + str(self.mSolutions[0])
            for s in range(1, len(self.mSolutions)):
                solutionString += (", " + str(self.mSolutions[s]))
            solutionString += "}"
        return objectStr + solutionString


    def OrderPlanesInTriangForm(self, allPlanes):
        return sorted(allPlanes, key=lambda item: item.GetZeroCoefficients()[0], reverse=False)

    def SolveForValue(self):
        while len(self.mSolutions) != len(self.mLiTempPlanes):
            for p in self.mLiTempPlanes:
                numNzs,nzCoordIndices = p.GetNonZeroCoefficients()
                if (numNzs == 1):
                    nonZeroIndex = nzCoordIndices[0]
                    self.mSolutions[nonZeroIndex] = round(p.mK/p.mNormalVector.mCoordinates[nonZeroIndex], 3)
                    for lclP in self.mLiTempPlanes:
                        lclP.InsertAndSolve(nonZeroIndex, self.mSolutions[nonZeroIndex])
                    break

    def AddEquations(self, srcEq, planeEqToSolve, solveForIdx):
        coefficient = -1
        if (srcEq.mNormalVector.mCoordinates[solveForIdx] != planeEqToSolve.mNormalVector.mCoordinates[solveForIdx]):
            coefficient = 1
        return planeEqToSolve + (srcEq*coefficient)

    def SolveSystem(self):
        numplanes = len(self.mLiTempPlanes)
        for i in range(0, numplanes-1):
            srcEq = self.mLiTempPlanes[i]
            srcEq.NormalizeCoefficient(i)
            for q in range(i+1, numplanes):
                if self.mLiTempPlanes[q].mNormalVector.mCoordinates[i] != 0:
                    planeEqToSolve = self.mLiTempPlanes[q]
                    planeEqToSolve.NormalizeCoefficient(i)
                    self.mLiTempPlanes[q] = self.AddEquations(srcEq, planeEqToSolve, i)
                    numNzs,nzCoordIndices = self.mLiTempPlanes[q].GetNonZeroCoefficients()
                    if numNzs == 0 and planeEqToSolve.mK != 0:
                        return
        self.mLiTempPlanes = self.OrderPlanesInTriangForm(self.mLiTempPlanes)
        self.SolveForValue()
                

