#include <iostream>
#include "tuple_impl_1.h"
#include "tuple_impl_2.h"
#include <string>
#include <tuple>

using StdTuple = std::tuple<int, std::string, double, int>;

void TestStdTuple()
{
  std::cout << "Test-1: Demo of standard Tuple implementation ...." << std::endl;

  StdTuple t(437, "This is a std::tuple implementation", 299.3243, 999999);
  std::cout << std::get<0>(t) << ", ";
  std::cout << std::get<1>(t) << ", ";
  std::cout << std::get<2>(t) << ", ";
  std::cout << std::get<3>(t) << std::endl;

  std::cout << "Now change the values of the tuple ..." << std::endl;
  std::get<0>(t) = 999;
  std::get<1>(t) = "std::string value has been changed";
  std::get<2>(t) = 934.1123;
  std::get<3>(t) = 11111;

  std::cout << std::get<0>(t) << ", ";
  std::cout << std::get<1>(t) << ", ";
  std::cout << std::get<2>(t) << ", ";
  std::cout << std::get<3>(t) << std::endl;
}

namespace MyOne
{
  using myTuple = Tuple<int, std::string, double, int>;

  void TestGetType()
  {
    std::cout << "\n\nTest-2: My tuple implementation (Method-1)...." << std::endl;
    GetType<0,myTuple>::Type s0 = 437;
    GetType<1,myTuple>::Type s1 = std::string("Test string");
    GetType<2,myTuple>::Type s2 = 299.3243;
    GetType<3,myTuple>::Type s3 = 'Z';
    std::cout << s0 << " - " << s1 << " - " << s2 << " - " << s3 << std::endl;
  }

  void TestGet()
  {
    myTuple t(437, "This is the actual tuple string", 299.3243, 999999);
    int v = Get<0>(t);
    std::cout << "Some get tests ..." << std::endl;
    std::cout << Get<0>(t) << ", ";
    std::cout << Get<1>(t) << ", ";
    std::cout << Get<2>(t) << ", ";
    std::cout << Get<3>(t) << std::endl;

    std::cout << "Some set tests ..." << std::endl;
    Get<0>(t) = 734;
    Get<1>(t) = "Replaced tuple string";
    Get<2>(t) = 992.3423;
    Get<3>(t) = 77777777;
    std::cout << Get<0>(t) << ", ";
    std::cout << Get<1>(t) << ", ";
    std::cout << Get<2>(t) << ", ";
    std::cout << Get<3>(t) << std::endl;
  }
}

namespace MyTwo
{
  using myTuple = Tuple<int, std::string, double, int>;

  void TestGetType()
  {
    std::cout << "\n\nTest-3: My tuple implementation (Method-2)...." << std::endl;
    GetType<0,myTuple>::Type s0 = 437;
    GetType<1,myTuple>::Type s1 = std::string("Test string");
    GetType<2,myTuple>::Type s2 = 299.3243;
    GetType<3,myTuple>::Type s3 = 'Z';
    std::cout << s0 << " - " << s1 << " - " << s2 << " - " << s3 << std::endl;
  }

  void TestGet()
  {
    myTuple t(437, "This is the actual tuple string", 299.3243, 999999);
    int v = Get<0>(t);
    std::cout << "Some get tests ..." << std::endl;
    std::cout << Get<0>(t) << ", ";
    std::cout << Get<1>(t) << ", ";
    std::cout << Get<2>(t) << ", ";
    std::cout << Get<3>(t) << std::endl;

    std::cout << "Some set tests ..." << std::endl;
    Get<0>(t) = 734;
    Get<1>(t) = "Replaced tuple string";
    Get<2>(t) = 992.3423;
    Get<3>(t) = 77777777;
    std::cout << Get<0>(t) << ", ";
    std::cout << Get<1>(t) << ", ";
    std::cout << Get<2>(t) << ", ";
    std::cout << Get<3>(t) << std::endl;
  }
}

int main()
{
  TestStdTuple();

  MyOne::TestGetType();
  MyOne::TestGet();

  MyTwo::TestGetType();
  MyTwo::TestGet();

  return 0;
}

