cmake_minimum_required(VERSION 3.5.1)
project(Mul-Library)

set (SRCS src/mul.cpp)

add_library(mul STATIC ${SRCS})

if (UNIX)
  target_compile_options(mul PUBLIC "-fPIC")
endif()

target_include_directories(mul PUBLIC inc)


