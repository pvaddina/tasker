#include "indent.h"
#include "indent_var_2.h"
#include "indent_var_3.h"
#include "indent_var_4.h"


int test_indent()
{
  std::cout << "+++ " << GetIndent<0>() << " +++" << std::endl;
  std::cout << "+++ " << GetIndent<1>() << " +++" << std::endl;
  std::cout << "+++ " << GetIndent<2>() << " +++" << std::endl;
  std::cout << "+++ " << GetIndent<3>() << " +++" << std::endl;
  std::cout << "+++ " << GetIndent<4>() << " +++" << std::endl;
  std::cout << "+++ " << GetIndent<5>() << " +++" << std::endl;
  std::cout << "+++ " << GetIndent<6>() << " +++" << std::endl;
  std::cout << "+++ " << GetIndent<7>() << " +++" << std::endl;

  // This will result in compilation static assert
  //std::cout << "+++ " << GetIndent<8>() << " +++" << std::endl;
  return 0;
}

int test_indent_2()
{
  // This is OK
  std::string s1 = VAR2::IString<9>();
  std::cout << s1 << "+++" << std::endl;

  // This will result in an error 
  // std::string s99999 = VAR2::IString<99999>();

  return 0;
}

int test_indent_3()
{
#if 0
  // This is OK
  std::string s1 = VAR3::IString<9>();
  std::cout << s1 << "+++" << std::endl;

  std::string s2 = VAR3::HString<10>();
  std::cout << s2 << "+++" << std::endl;

  // This will result in an error 
  // std::string s99999 = VAR3::IString<99999>();
#endif
  return 0;
}

int test_indent_4()
{
#if 0
  // This is OK
  std::string s1 = VAR4::IString<9>();
  std::cout << s1 << "+++" << std::endl;

  std::string s2 = VAR4::HString<10>();
  std::cout << s2 << "+++" << std::endl;

  // This will result in an error 
  // std::string s99999 = VAR4::IString<99999>();
#endif

  return 0;
}


int main()
{
  test_indent();
  test_indent_2();
  test_indent_3();
  test_indent_4();
  return 0;
}


