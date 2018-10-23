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

  namespace Type1
  {
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

    // Make a string out of all the arguments and print them out on std::cout
    template <typename... Ts>
    static void POut(Ts... ts)
    {
      std::string s = MkStr(ts...);
      std::cout << s;
    }
  }

  namespace Type2
  {
    // Make a string out of all the arguments passed here. Uses, std::stringstream. 
    template <typename T, typename U>
    void PrintToSStream(T& s, U&& val)
    {
      s << val << " ";
    }

    template <typename T, typename U, typename... Ts>
    void PrintToSStream(T& s, U&& val, Ts&&... ts)
    {
      s << val << " ";
      PrintToSStream(s, ts...);
    }

    template <typename T, typename... Ts>
    std::string Print(Ts&&... ts)
    {
      T s;
      PrintToSStream(s, ts...);
      std::cout << s.str() << std::endl;
    }

    template <typename... Ts>
    void POut(Ts&&... ts)
    {
      Print<std::stringstream>(ts...);
    }
  }

};

