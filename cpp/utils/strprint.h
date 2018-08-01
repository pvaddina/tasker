#pragma once

#include <iostream>
#include <sstream>

// A structure with static functions that generate a string based on the 
// passed values irrespective of the type
namespace PUtils
{
#if 0
  // Looks fine but this is not a good idea. Firstly the client definitions are
  // to be included here. Secondly this will not work and will lead to 
  // compiler ambiguity as to which operator it needs to call (the one
  // in std, or this one) because T could be replaced by anything. 
  // 
  // Can we achieve this using enable_if ???? 
  // The form as given below did not work though
  //
  template <typename T,
            typename std::enable_if_t<std::is_fundamental<T>::value> >
  std::ostream& operator<<(std::ostream& os, const T& obj)
  {
    obj.POut(os);
    return os;
  }
#endif

  // Make a string out of all the arguments passed here. Uses, std::stringstream. 
  template <typename T>
  static std::string MkStr(T val)
  {
    std::stringstream s;
    s << val;
    return s.str();
  }

  template <typename T, typename... Ts>
  static std::string MkStr(T val, Ts... ts)
  {
    std::stringstream s;
    s << val << MkStr(ts...);
    return s.str();
  }

  // Make a empty string with the defined number of spaces
  template <int N>
  static std::string MkEmptyStr()
  {
    return std::string(" ") + MkEmptyStr<N-1>();
  }

  template <>
  static std::string MkEmptyStr<1>()
  {
    return std::string(" ");
  }

  template <>
  static std::string MkEmptyStr<0>()
  {
    return std::string("");
  }

  // Make a string out of all the arguments and print them out on std::cout
  template <typename... Ts>
  static void POut(Ts... ts)
  {
    std::string s = MkStr(ts...);
    std::cout << s;
  }


  // Insert the passed number of spaces followed by the string
  template <int N>
  static void EOut(const std::string s)
  {
    std::string ident = MkEmptyStr<N>();
    std::cout << ident << s;
  }
};

