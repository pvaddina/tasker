import sys
sys.path.insert(0, '../vector')

import vector as vec
import line


def PrintResult_Task7(orientation, intersectPts):
    if orientation == vec.Orientation.INTERSECTING:
        print("Intersecting lines with coordinates")
        print(intersectPts)
    elif orientation == vec.Orientation.ORTHOGONAL:
        print("Lines are Orthogonal")
    elif orientation == vec.Orientation.PARALLEL:
        print("Lines are Parallel")
    elif orientation == vec.Orientation.PARALLEL_AND_SAME:
        print("Lines are Parallel and Same")
    else:
        print("Lines are Orthogonal and Parallel")


def Task7_LineIntersections():
    print("###################################################")
    l1 = line.Line([4.046, 2.836], 1.21)
    l2 = line.Line([10.115, 7.09], 3.025)

    l3 = line.Line([7.204, 3.182], 8.68)
    l4 = line.Line([8.172, 4.114], 9.883)

    l5 = line.Line([1.182, 5.562], 6.744)
    l6 = line.Line([1.773, 8.343], 9.525)

    orientation12, intersect12 = l1.GetIntersection(l2)
    orientation34, intersect34 = l3.GetIntersection(l4)
    orientation56, intersect56 = l5.GetIntersection(l6)

    PrintResult_Task7(orientation12, intersect12)
    PrintResult_Task7(orientation34, intersect34)
    PrintResult_Task7(orientation56, intersect56)


def TestSimpleLines():
    print("###################################################")
    l1 = line.Line([0, 2], 10)
    l2 = line.Line([0, 16], 80)
    orientation, intersect = l1.GetIntersection(l2)
    PrintResult_Task7(orientation, intersect)

    l1 = line.Line([0, 2], 10)
    l2 = line.Line([0, 15], 80)
    orientation, intersect = l1.GetIntersection(l2)
    PrintResult_Task7(orientation, intersect)

    l1 = line.Line([2, 0], 10)
    l2 = line.Line([16, 0], 80)
    orientation, intersect = l1.GetIntersection(l2)
    PrintResult_Task7(orientation, intersect)

    l1 = line.Line([2, 0], 10)
    l2 = line.Line([15, 0], 80)
    orientation, intersect = l1.GetIntersection(l2)
    PrintResult_Task7(orientation, intersect)

    l1 = line.Line([2, 0], 10)
    l2 = line.Line([0, 16], 80)
    orientation, intersect = l1.GetIntersection(l2)
    PrintResult_Task7(orientation, intersect)

Task7_LineIntersections()
TestSimpleLines()


