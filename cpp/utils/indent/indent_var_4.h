#include <iostream>
#include <string>
#include <functional>
#include <memory>
#include <type_traits>

namespace VAR4
{
  static const std::string IndentSpaces[] = { 
    "   ",
    "      ",
    "         ",
    "            ",
    "               ",
    "                  ",
    "                     ",
    "                        ",
    "                           ",
    "                              ",
    "                                 ",
  };

  static const std::string HashSpaces[] = { 
    "###",
    "######",
    "#########",
    "############",
    "###############",
  };

  // Make a empty string with the defined number of spaces
  template <typename T, const T* ARRAY, size_t SZ, int N>
    static std::enable_if_t< (N > SZ-1), void > MkEmptyStr() 
    {
      static_assert(true, "Invalid array index");
    }

  template <typename T, const T* ARRAY, size_t SZ, int N>
    static std::enable_if_t< (N <= SZ-1), T > MkEmptyStr()
    {
      return ARRAY[N];
    }

  template <size_t N>
    auto IString = MkEmptyStr<std::string, IndentSpaces, sizeof(IndentSpaces), N>; 

  template <size_t N>
    auto HString = MkEmptyStr<std::string, HashSpaces, sizeof(HashSpaces), N>; 
}
