#include <pybind11/pybind11.h>

namespace py = pybind11;

#include "add.h"
#include "mul.h"
#include "hello.h"

PYBIND11_MODULE(cahello, m) {
	m.doc() = "pybind11 example plugin"; // optional module docstring
	m.def("add", &add, "A function which adds two numbers");
	m.def("mul", &mul, "A function which multiplies two numbers");
	py::class_<SayHello> hello{ m, "SayHello" };
	hello.def(py::init<const int&>())
		.def("InHindi", &SayHello::InHindi)
		.def("InTelugu", &SayHello::InTelugu)
		.def("InChinese", &SayHello::InChinese)
		.def("InEnglish", &SayHello::InEnglish);
}
