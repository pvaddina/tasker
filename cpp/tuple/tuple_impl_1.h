#include <type_traits>

namespace MyTwo
{
  //////////////////////////////////////////////////////////
  // 1. Template definition
  //////////////////////////////////////////////////////////
  template <typename... Ts> struct Tuple;

  template <typename T, typename... Ts>
  struct Tuple<T, Ts...> : public Tuple<Ts...>
  {
    Tuple(T t, Ts... ts) : Tuple<Ts...>(ts...), mVal(t) {}
    T mVal;
  };

  template <typename T>
  struct Tuple<T>
  {
    Tuple(T t) : mVal(t) {}
    T mVal;
  };


  //////////////////////////////////////////////////////////
  // GetType at an index
  //////////////////////////////////////////////////////////
  template <size_t i, typename... Ts> struct GetType;

  template <size_t i, typename T, typename... Ts> 
  struct GetType<i, Tuple<T,Ts...> > 
  {
    using Type = typename GetType<i-1, Tuple<Ts...> >::Type;
  };

  template <typename T, typename... Ts>
  struct GetType<0, Tuple<T,Ts...> >
  {
    using Type = T;
  };


  //////////////////////////////////////////////////////////
  // Get value at a given index
  //////////////////////////////////////////////////////////
  template <size_t i, typename... Ts>
  typename std::enable_if<i==0, typename GetType<i,Tuple<Ts...> >::Type&>::type 
  Get(Tuple<Ts...>& t)
  {
    return t.mVal;
  }

  template <size_t i, typename T, typename... Ts>
  typename std::enable_if<i!=0, typename GetType<i,Tuple<T,Ts...> >::Type&>::type 
  Get(Tuple<T,Ts...>& t)
  {
    Tuple<Ts...>& base(t);
    return Get<i-1>(base);
  }
}
