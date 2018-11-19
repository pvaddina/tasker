cmake_minimum_required(VERSION 3.5.1)
project(Pywrapper-with-pybind11)
include(../CMakeInclude.cmake)

set (SRCS pybind.cpp)

add_pybind_subdirectory()

pybind11_add_module(pb MODULE ${SRCS})


