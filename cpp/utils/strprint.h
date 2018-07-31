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
    obj.Print(os);
    return os;
  }
#endif


  template <typename T>
  static std::string GetStr(T val)
  {
    std::stringstream s;
    s << val;
    return s.str();
  }

  template <typename T, typename... Ts>
  static std::string GetStr(T val, Ts... ts)
  {
    std::stringstream s;
    s << val << GetStr(ts...);
    return s.str();
  }

  template <typename... Ts>
  static void Print(Ts... ts)
  {
    std::cout << GetStr(ts...);
  }
};

