#include <iostream>
#include <string>
#include <functional>
#include <memory>
#include <type_traits>

namespace VAR2

{
  template<typename T, size_t SZ>
    constexpr auto GetLen(T (&) [SZ]) 
    { 
      return SZ; 
    }


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

  // Make a empty string with the defined number of spaces
  template <int N>
    static std::enable_if_t< (N > GetLen(IndentSpaces)-1), std::string > IString() 
    {
      static_assert((N <= GetLen(IndentSpaces)-1), "OUT OF BOUNDS");
      return "";
    }

  template <int N>
    static std::enable_if_t< (N <= GetLen(IndentSpaces)-1), std::string > IString()
    {
      return IndentSpaces[N];
    }
}
