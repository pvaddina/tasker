import plane

class LinearSystem(object):
    def __init__(self, liPlanes):
        try:
            d = liPlanes[0].mDimension
            for p in liPlanes:
                assert d == p.mDimension            
            # Save the planes. But before that make sure the equations are sorted according to the
            # number of non-zero coefficients, in increasing order
            self.mLiPlanes = liPlanes
            self.mLiTempPlanes = liPlanes
            self.OrderPlanesInTriangForm()
            self.mSolutions = {}
        except AssertionError:
            raise Exception("All planes do not have the same Dimensions")

    def __len__(self):
        return len(self.mLiPlanes)

    def __str__(self):
        return "A linear system with {} Planes".format(self.__len__())

    def OrderPlanesInTriangForm(self):
        self.mLiTempPlanes = sorted(self.mLiTempPlanes, key=lambda item: item.mDimension, reverse=True)

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
        numplanes = len(self.mLiPlanes)
        for i in range(0, numplanes-1):
            srcEq = self.mLiTempPlanes[i]
            srcEq.NormalizeCoefficient(i)
            for q in range(i+1, numplanes):
                planeEqToSolve = self.mLiTempPlanes[q]
                planeEqToSolve.NormalizeCoefficient(i)
                self.mLiTempPlanes[q] = self.AddEquations(srcEq, planeEqToSolve, i)
        self.OrderPlanesInTriangForm()
        self.SolveForValue()
        printStr = "Solutions for the system: {" + str(self.mSolutions[0])
        for s in range(1, len(self.mSolutions)):
            printStr += (", " + str(self.mSolutions[s]))
        printStr += "}"
        print(printStr)
                

