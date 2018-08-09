#include <iostream>
#include <string>
#include <functional>
#include <memory>
#include <type_traits>

#if 0
  template<typename T, std::size_t SZ>
    constexpr std::size_t GetLen(T (&) [SZ]) 
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
  template <typename T, const std::vector<T>& ARRAY, size_t SZ, int N>
    static std::string GetItem()
    {
      //static_assert(N >= SZ, "Out of bounds");
      return IndentSpaces[N];
    }

  template <size_t N>
    auto IString = GetItem<std::string, IndentSpaces, GetLen(IndentSpaces), N>;
#endif

