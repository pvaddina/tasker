#include <iostream>
#include <string>
#include <functional>
#include <memory>
#include <type_traits>

static constexpr char* IndentSpaces[] = { 
                                (char*)"zero",
                                (char*)"one",
                                (char*)"two",
                                (char*)"three",
                                (char*)"four",
                                (char*)"five",
                                (char*)"six",
                                (char*)"seven"
                              };


template<typename T, size_t SZ>
constexpr auto GetLen(T (&) [SZ]) 
{ 
    return SZ; 
}

template<typename T, size_t SZ>
struct ArrayWrapper
{
    constexpr ArrayWrapper(T(&aptr)[SZ]) : ptr(aptr) {}
    T(&ptr)[SZ];
};

template<typename T, size_t SZ>
constexpr auto GetVal(T (&array) [SZ], size_t N) 
{ 
    //static_assert(N >= SZ, "OUT OF BOUNDS");
    return ArrayWrapper<T, SZ>{array}.ptr[N]; 
}

template<size_t IDX>
constexpr auto GetIndent() 
{
    static_assert(IDX < GetLen(IndentSpaces), "OUT OF BOUNDS");
    return GetVal(IndentSpaces, IDX);
}
