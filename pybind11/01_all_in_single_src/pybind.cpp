#include <pybind11/pybind11.h>

#if 0
#include "add.h"
#include "mul.h"
#else
int add(int i, int j) {
    return i + j;
}

int mul(int i, int j) {
    return i * j;
}
#endif

PYBIND11_MODULE(pb, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("add", &add, "A function which adds two numbers");
    m.def("mul", &mul, "A function which multiplies two numbers");
}
