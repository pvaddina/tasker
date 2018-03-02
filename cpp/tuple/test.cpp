#include <iostream>
#include "tuple.h"
#include <string>
#include <tuple>

using myTuple = my::tuple<int, std::string, double, int>;
using StdTuple = std::tuple<int, std::string, double, int>;

void TestStdTuple()
{
  std::cout << "Test-1: Demo of standard Tuple implementation ...." << std::endl;

  StdTuple t(437, "This is a std::tuple implementation", 299.3243, 999999);
  std::cout << "Value at index-" << 0 << ": " << std::get<0>(t) << std::endl;
  std::cout << "Value at index-" << 1 << ": " << std::get<1>(t) << std::endl;
  std::cout << "Value at index-" << 2 << ": " << std::get<2>(t) << std::endl;
  std::cout << "Value at index-" << 3 << ": " << std::get<3>(t) << std::endl;

  std::cout << "Now change the values of the tuple ..." << std::endl;
  std::get<0>(t) = 999;
  std::get<1>(t) = "std::string value has been changed";
  std::get<2>(t) = 934.1123;
  std::get<3>(t) = 11111;

  std::cout << "Value at index-" << 0 << " after value change: " << std::get<0>(t) << std::endl;
  std::cout << "Value at index-" << 1 << " after value change: " << std::get<1>(t) << std::endl;
  std::cout << "Value at index-" << 2 << " after value change: " << std::get<2>(t) << std::endl;
  std::cout << "Value at index-" << 3 << " after value change: " << std::get<3>(t) << std::endl;
}

void TestGetType()
{
  std::cout << std::endl << "Test-2: Demo of my::tuple my::GetType utility class ...." << std::endl;
  my::GetType<0,myTuple>::Type s0 = 437;
  my::GetType<1,myTuple>::Type s1 = std::string("Test string");
  my::GetType<2,myTuple>::Type s2 = 299.3243;
  my::GetType<3,myTuple>::Type s3 = 'Z';
  std::cout << s0 << " - " << s1 << " - " << s2 << " - " << s3 << std::endl;
}

void TestGet()
{
  std::cout << std::endl << "Test-3: Demo of my::tuple my::Get utility function ...." << std::endl;
  myTuple t(437, "This is my::tuple implementation", 299.3243, 999999);
  int v = my::Get<0>(t);
  std::cout << "Value at index-" << 0 << ": " << my::Get<0>(t) << std::endl;
  std::cout << "Value at index-" << 1 << ": " << my::Get<1>(t) << std::endl;
  std::cout << "Value at index-" << 2 << ": " << my::Get<2>(t) << std::endl;
  std::cout << "Value at index-" << 3 << ": " << my::Get<3>(t) << std::endl;

#if 0
  std::cout << "Now change the values of the my::tuple ..." << std::endl;
  my::Get<0>(t) = 999;
  my::Get<1>(t) = "std::string value has been changed";
  my::Get<2>(t) = 934.1123;
  my::Get<3>(t) = 11111;

  std::cout << "Value at index-" << 0 << " after value change: " << my::Get<0>(t) << std::endl;
  std::cout << "Value at index-" << 1 << " after value change: " << my::Get<1>(t) << std::endl;
  std::cout << "Value at index-" << 2 << " after value change: " << my::Get<2>(t) << std::endl;
  std::cout << "Value at index-" << 3 << " after value change: " << my::Get<3>(t) << std::endl;
#endif
}


int main()
{
  TestStdTuple();
  TestGetType();
  TestGet();

  return 0;
}

