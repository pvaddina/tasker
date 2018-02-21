#include <iostream>
#include "tuple.h"
#include <string>

using myTuple = my::tuple<int, std::string, double, int>;

void TestGetType()
{
  my::GetType<0,myTuple>::Type s0 = 437;
  my::GetType<1,myTuple>::Type s1 = std::string("Test string");
  my::GetType<2,myTuple>::Type s2 = 299.3243;
  my::GetType<3,myTuple>::Type s3 = 'Z';
  std::cout << s0 << " - " << s1 << " - " << s2 << " - " << s3 << std::endl;
}

void TestGet()
{
  myTuple t(437, "This is the actual tuple string", 299.3243, 999999);
  int v = my::Get<0>(t);
  std::cout << my::Get<0>(t) << std::endl;
  std::cout << my::Get<1>(t) << std::endl;
  std::cout << my::Get<2>(t) << std::endl;
  std::cout << my::Get<3>(t) << std::endl;
}


int main()
{
  TestGetType();
  TestGet();

  return 0;
}

