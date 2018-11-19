cmake_minimum_required(VERSION 3.5.1)
project(Add-Library)

set (SRCS src/add.cpp )

add_library(add STATIC ${SRCS})

if (UNIX)
  target_compile_options(add PUBLIC "-fPIC")
endif()

target_include_directories(add PUBLIC inc)


