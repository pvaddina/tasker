namespace my
{
  //////////////////////////////////////////////////////////
  // 1. Template definition
  //////////////////////////////////////////////////////////
  template <typename... Ts> struct tuple;

  template <typename T, typename... Ts>
  struct tuple<T, Ts...> : public tuple<Ts...>
  {
    tuple(T t, Ts... ts) : tuple<Ts...>(ts...), mVal(t) {}
    T mVal;
  };

  template <typename T>
  struct tuple<T>
  {
    tuple(T t) : mVal(t) {}
    T mVal;
  };


  //////////////////////////////////////////////////////////
  // GetType at an index
  //////////////////////////////////////////////////////////
  template <size_t i, typename... Ts> struct GetType;

  template <size_t i, typename T, typename... Ts> 
  struct GetType<i, tuple<T,Ts...> > 
  {
    using Type = typename GetType<i-1, tuple<Ts...> >::Type;
  };

  template <typename T, typename... Ts>
  struct GetType<0, tuple<T,Ts...> >
  {
    using Type = T;
  };


  //template <size_t i, typename... Ts>
  //using RetTyp = typename GetType<i,tuple<T,Ts...> >::Type 

  //////////////////////////////////////////////////////////
  // Get value at a given index
  //////////////////////////////////////////////////////////
  template <size_t i, typename... Ts> struct GetValue;

  template <size_t i, typename T, typename... Ts> 
  struct GetValue<i, tuple<T,Ts...> > 
  {
    static typename GetType<i,tuple<T,Ts...> >::Type Get(tuple<T,Ts...>& t)
    {
      return GetValue<i-1, tuple<Ts...> >::Get(t);
    }
  };

  template <typename T, typename... Ts>
  struct GetValue<0, tuple<T,Ts...> >
  {
    static typename GetType<0,tuple<T,Ts...> >::Type Get(tuple<T,Ts...>& t)
    {
      return (static_cast<tuple<T, Ts...> >(t)).mVal;
    }  
  };

  template <size_t i, typename... Ts>
  typename GetType<i,tuple<Ts...> >::Type Get(tuple<Ts...>& t)
  {
    return GetValue<i, tuple<Ts...> >::Get(t);
  }
}
