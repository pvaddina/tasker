namespace My
{
  template <typename... Ts>
  struct Any
  {
  };

  template <size_t i, typename... Ts> struct GetType;

  template <size_t i, typename T, typename... Ts, template <typename,typename...> typename S>
  struct GetType<i, S<T,Ts...> >
  {
    using Type = typename GetTpe<i-1, S<Ts...> >::Type;
  };

  template <typename T, typename... Ts, template <typename,template...> typename S>
  struct GetType<0, S<T,Ts...> >
  {
    using Type = T;
  };

}
