namespace MyOne
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
  template <size_t i, typename... Ts> struct GetValue;

  template <size_t i, typename T, typename... Ts> 
  struct GetValue<i, Tuple<T,Ts...> > 
  {
    static typename GetType<i,Tuple<T,Ts...> >::Type& Get(Tuple<T,Ts...>& t)
    {
      return GetValue<i-1, Tuple<Ts...> >::Get((Tuple<Ts...>&)t);
    }
  };

  template <typename T, typename... Ts>
  struct GetValue<0, Tuple<T,Ts...> >
  {
    static typename GetType<0,Tuple<T,Ts...> >::Type& Get(Tuple<T,Ts...>& t)
    {
      return t.mVal;
    }  
  };

  template <size_t i, typename... Ts>
  typename GetType<i,Tuple<Ts...> >::Type& Get(Tuple<Ts...>& t)
  {
    return GetValue<i, Tuple<Ts...> >::Get(t);
  }

}
