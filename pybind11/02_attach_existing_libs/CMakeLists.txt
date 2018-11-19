cmake_minimum_required(VERSION 3.5.1)
project(Calculator-Library)

add_subdirectory(add_lib)
add_subdirectory(mul_lib)
add_subdirectory(hello)

include(../CMakeInclude.cmake)

add_pybind_subdirectory()

add_library(cahello MODULE pb_cahello.cpp)
target_link_libraries(cahello PRIVATE add mul hello pybind11::module)
set_target_properties(cahello PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}"
                                         SUFFIX "${PYTHON_MODULE_EXTENSION}")

