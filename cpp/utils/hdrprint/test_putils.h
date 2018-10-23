#include <string>
#include "strprint.h"

namespace Test1
{
  void Test1()
  {
    std::string s = PUtils::Type1::MkStr("Test1", 23, 'x', "some string");
    std::cout << s << std::endl;
  }
}

namespace Test2
{
  void Test2()
  {
    PUtils::Type1::POut("Test2-", 23, 'x', "some string\n");
    PUtils::Type1::POut("Test2-", 23);

    PUtils::Type2::POut("Test2-", 23, 'x', "some string\n");
  }
}

struct RandomS
{
public:
  RandomS(const int i, const std::string& s) : one(i), two(s) {}

  void POut(std::ostream& os) const
  {
    os << one << " " << two;
  }

  std::ostream& operator<<(std::ostream& os)
  {
    POut(os);
    return os;
  }

private:
  int one;
  std::string two;
};

std::ostream& operator<<(std::ostream& os, const RandomS& obj)
{
  obj.POut(os);
  return os;
}

namespace Test3
{
  void Test3()
  {
    RandomS r{437, "Rollnumber"};
    PUtils::Type1::POut(23, 'x', r, "some string\n");
  }
}

namespace Test4
{
  void Test4()
  {
    constexpr int i = 437;
    RandomS r{437, "Rollnumber"};
    PUtils::Type1::POut("The value of i = ", i, ", not ", 34.2324, r, "(just for info)");
  }
}



int Printtest()
{
  Test1::Test1();
  Test2::Test2();
  std::cout << "\n\n";
  Test3::Test3();
  Test4::Test4();
  return 0;
}



