cmake_minimum_required(VERSION 3.5.1)
project(Hello-World)

set(SRCS priv/hello.cpp)

add_library(hello STATIC ${SRCS})

if (UNIX)
  target_compile_options(hello PUBLIC "-fPIC")
endif()

target_include_directories(hello PUBLIC pub)

