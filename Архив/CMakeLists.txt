cmake_minimum_required(VERSION 3.20)
project(Study)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(informaticts)

add_executable(Study
        informaticts/1.cpp
        informaticts/9.1.cpp
        main.cpp)
