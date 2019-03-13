import vector as vec


def SimpleTest1():
    print("###################################################")
    v = vec.Vector([2,3,4])
    print(v)

def VecPlusSubMul():
    print("###################################################")
    addRes = vec.Vector([8.218, -9.341]) + vec.Vector([-1.129, 2.111])
    print("Add result = {}".format(addRes))
    subRes = vec.Vector([7.119, 8.215]) - vec.Vector([-8.223, 0.878])
    print("Sub result = {}".format(subRes))
    mulRes = vec.Vector([1.671, -1.012, -0.318]) * 7.41
    print("Mul result = {}".format(mulRes))

def Task3():
    print("###################################################")
    v1 = vec.Vector([-0.221, 7.437])
    v2 = vec.Vector([8.813, -1.331, -6.247])
    v3 = vec.Vector([5.581, -2.136])
    v4 = vec.Vector([1.996, 3.108, -4.554])
    print(v1.Magnitude())
    print(v2.Magnitude())
    v3.Normalize()
    v4.Normalize()
    print("v3 Normalized = {}".format(v3))
    print("v4 Normalized = {}".format(v4))

def Task4():
    print("###################################################")
    dp1 = vec.Vector([7.887,4.138]).DotProduct(vec.Vector([-8.802, 6.776]))
    dp2 = vec.Vector([-5.955,-4.904,-1.874]).DotProduct(vec.Vector([-4.496,-8.755,7.103]))
    rad = vec.Vector([3.183, -7.627]).AngleRad(vec.Vector([-2.668,5.319]))
    deg = vec.Vector([7.35, 0.221, 5.188]).AngleDeg(vec.Vector([2.751,8.259,3.985]))
    print("dp1=%4.3f" % dp1)
    print("dp2=%4.3f" % dp2)
    print("rad=%4.3f" % rad)
    print("deg=%4.3f" % deg)

def Task5():
    print("###################################################")
    print(vec.Vector([-7.579, -7.88]).GetOrientation(vec.Vector([22.737, 23.64])))
    print(vec.Vector([-2.029, 9.97, 4.172]).GetOrientation(vec.Vector([-9.231, -6.639, -7.245])))
    print(vec.Vector([-2.328, -7.284, -1.214]).GetOrientation(vec.Vector([-1.821, 1.072, -2.94])))
    print(vec.Vector([-2.118, 4.827]).GetOrientation(vec.Vector([0,0])))


def Task6_CrossProducts():
    print("###################################################")
    v1 = vec.Vector([1,2,3])
    v2 = vec.Vector([4,5,6])
    cp = vec.Vector(v1.CrossProduct(v2))
    print(cp.DotProduct(v1))
    print(cp.DotProduct(v2))

    v3 = vec.Vector([8.462, 7.893, -8.187])
    w3 = vec.Vector([6.984, -5.975, 4.778])
    v4 = vec.Vector([-8.987, -9.838, 5.031])
    w4 = vec.Vector([-4.268, -1.861, -8.866])
    v5 = vec.Vector([1.5, 9.547, 3.691])
    w5 = vec.Vector([-6.007, 0.124, 5.772])

    print(v3.CrossProduct(w3))  
    print(v4.ParallelogramArea(w4))
    print(v5.TriangleArea(w5))


SimpleTest1()
VecPlusSubMul()
Task3()
Task4()
Task5()
Task6_CrossProducts()


