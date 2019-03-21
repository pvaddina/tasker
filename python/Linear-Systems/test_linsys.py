import plane as pl
import linsys as ls

def TestUnique_1():
    print("###################################################")
    p1 = pl.Plane([-1, 1, 1], -2)
    p2 = pl.Plane([1, -4, 4], 21)
    p3 = pl.Plane([7, -5, -11], 0)

    lSys = ls.LinearSystem([p1, p2, p3])
    lSys.SolveSystem()
    print(str(lSys))

def TestUnique_2():
    print("###################################################")
    p1 = pl.Plane([1, 1, 0], 1)
    p2 = pl.Plane([0, 1, 1], 0)
    p3 = pl.Plane([0, 0, 1], -1)

    lSys = ls.LinearSystem([p1, p2, p3])
    lSys.SolveSystem()
    print(str(lSys))

def TestUnique_3():
    print("###################################################")
    p1 = pl.Plane([0, 1, -1], 2)
    p2 = pl.Plane([1, -1, 1], 2)
    p3 = pl.Plane([3, -4, 1], 1)

    lSys = ls.LinearSystem([p1, p2, p3])
    lSys.SolveSystem()
    print(str(lSys))

def TestUnique_FourEqs_4():
    print("###################################################")
    p1 = pl.Plane([1, 1, 0], 1)
    p2 = pl.Plane([0, 1, 1], 0)
    p3 = pl.Plane([0, 0, 1], -1)
    p4 = pl.Plane([1, 3, 2], 1)

    lSys = ls.LinearSystem([p1, p2, p3, p4])
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



TestUnique_1()
TestUnique_2()
TestUnique_3()
TestUnique_FourEqs_4()
Test_NoSolution()


