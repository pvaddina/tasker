import plane as pl
import linsys as ls

def Test1():
    print("###################################################")
    p1 = pl.Plane([-1, 1, 1], -2)
    p2 = pl.Plane([1, -4, 4], 21)
    p3 = pl.Plane([7, -5, -11], 0)

    lSys = ls.LinearSystem([p1, p2, p3])
    lSys.SolveSystem()
    print(str(lSys))

def Test2():
    print("###################################################")
    p1 = pl.Plane([0, 1, -1], 2)
    p2 = pl.Plane([1, -1, 1], 2)
    p3 = pl.Plane([3, -4, 1], 1)

    lSys = ls.LinearSystem([p1, p2, p3])
    lSys.SolveSystem()
    print(str(lSys))

def Test_NoSolution():
    print("###################################################")
    p1 = pl.Plane([1, -2, 1], 1)
    p2 = pl.Plane([1, 0, -2], 2)
    p3 = pl.Plane([-1, 4, -4], 0)

    lSys = ls.LinearSystem([p1, p2, p3])
    lSys.SolveSystem()
    print(str(lSys))



Test1()
Test2()
Test_NoSolution()


