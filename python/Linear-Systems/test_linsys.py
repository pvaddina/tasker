import plane as pl
import linsys as ls

def Test1_LinearSystemsTest():
    print("###################################################")
    p1 = pl.Plane([-0.412, 3.806, 0.728], -3.46)
    p2 = pl.Plane([1.03, -9.515, -1.82], 8.65)

    p3 = pl.Plane([2.611, 5.528, 0.283], 4.6)
    p4 = pl.Plane([7.715, 8.306, 5.342], 3.76)

    p5 = pl.Plane([-7.926, 8.625, -7.217], -7.952)
    p6 = pl.Plane([-2.692, 2.875, -2.404], -2.443)

    lSys = ls.LinearSystem([p1, p2, p3, p4, p5, p6])
    print("Number of pls: {}".format(len(lSys)))
    print(str(lSys))


def Test2_VerySimpleLinearSystem():
    p1 = pl.Plane([1, 0, 0], 1)
    p2 = pl.Plane([0, 1, 0], 2)
    p3 = pl.Plane([0, 0, 1], 3)

    lSys = ls.LinearSystem([p1, p2, p3])
    lSys.SolveSystem()

#Test1_LinearSystemsTest()
Test2_VerySimpleLinearSystem()


