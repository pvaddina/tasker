import sys
sys.path.insert(0, '../vector')

import vector as vec
import plane


def PrintResult_Task7(orientation, intersectPts):
    if orientation == vec.Orientation.INTERSECTING:
        print("Intersecting planes with coordinates")
    elif orientation == vec.Orientation.ORTHOGONAL:
        print("Planes are Orthogonal")
    elif orientation == vec.Orientation.PARALLEL:
        print("Planes are Parallel")
    elif orientation == vec.Orientation.PARALLEL_AND_SAME:
        print("Planes are Parallel and Same")
    else:
        print("Planes are Orthogonal and Parallel")


def Task7_PlaneIntersections():
    print("###################################################")
    p1 = plane.Plane([-0.412, 3.806, 0.728], -3.46)
    p2 = plane.Plane([1.03, -9.515, -1.82], 8.65)

    p3 = plane.Plane([2.611, 5.528, 0.283], 4.6)
    p4 = plane.Plane([7.715, 8.306, 5.342], 3.76)

    p5 = plane.Plane([-7.926, 8.625, -7.217], -7.952)
    p6 = plane.Plane([-2.692, 2.875, -2.404], -2.443)

    orientation12, intersect12 = p1.GetIntersection(p2)
    orientation34, intersect34 = p3.GetIntersection(p4)
    orientation56, intersect56 = p5.GetIntersection(p6)

    PrintResult_Task7(orientation12, intersect12)
    PrintResult_Task7(orientation34, intersect34)
    PrintResult_Task7(orientation56, intersect56)


Task7_PlaneIntersections()


