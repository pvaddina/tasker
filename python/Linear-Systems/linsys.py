import plane

class LinearSystem(object):
    def __init__(self, liPlanes):
        try:
            d = liPlanes[0].mDimension
            for p in liPlanes:
                assert d == p.mDimension

            self.mLiPlanes = liPlanes
            self.mLiTempPlanes = liPlanes
            self.mSolutions = {}
        except AssertionError:
            raise Exception("All planes do not have the same Dimensions")

    def __len__(self):
        return len(self.mLiPlanes)

    def __str__(self):
        return "A linear system with {} Planes".format(self.__len__())

    def Solve(self):
        while len(self.mSolutions) != len(self.mLiTempPlanes):
            for p in self.mLiTempPlanes:
                numNzs,nzCoordIndices = p.GetNonZeroCoefficients()
                if (numNzs == 1):
                    nonZeroIndex = nzCoordIndices[0]
                    self.mSolutions[nonZeroIndex] = round(p.mK/p.mNormalVector[nonZeroIndex], 3)
                    for lclP in self.mLiTempPlanes:
                        lclP.InsertAndSolve(nonZeroIndex, self.mSolutions[nonZeroIndex])
                    break        

    def SolveSystem(self):
        self.Solve()

        
                

