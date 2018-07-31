#include <string>
#include "strprint.h"

namespace Test1
{
  void Test1()
  {
    std::string s = PUtils::GetStr(23, 'x', "some string");
    std::cout << s << std::endl;
  }
}

namespace Test2
{
  void Test2()
  {
    PUtils::Print(23, 'x', "some string\n");
    PUtils::Print(23);
  }
}

namespace Test3
{
  struct RandomS
  {
    public:
    RandomS(const int i, const std::string& s) : one(i), two(s) {}

    void Print(std::ostream& os) const
    {
      os << one << " " << two;
    }

    std::ostream& operator<<(std::ostream& os)
    {
      Print(os);
      return os;
    }

    private:
      int one;
      std::string two;
  };

  std::ostream& operator<<(std::ostream& os, const RandomS& obj)
  {
    obj.Print(os);
    return os;
  }

  void Test3()
  {
    RandomS r{437, "Rollnumber"};
    PUtils::Print(23, 'x', r, "some string\n");
  }
}

int Printtest()
{
  Test1::Test1();
  Test2::Test2();
  std::cout << "\n\n";
  Test3::Test3();
  return 0;
}



