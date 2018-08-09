#include "indent.h"
#include "indent_var_2.h"
#include "indent_var_3.h"
#include "indent_var_4.h"


#if 0
int test_indent()
{
  // This is OK
  std::string s1 = IString<9>();
  std::cout << s1 << "+++" << std::endl;

  // This will result in an error 
  // std::string s99999 = IString<99999>();

  return 0;
}
#endif

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
  // This is OK
  std::string s1 = VAR3::IString<9>();
  std::cout << s1 << "+++" << std::endl;

  std::string s2 = VAR3::HString<10>();
  std::cout << s2 << "+++" << std::endl;

  // This will result in an error 
  // std::string s99999 = VAR3::IString<99999>();

  return 0;
}

int test_indent_4()
{
  // This is OK
  std::string s1 = VAR4::IString<9>();
  std::cout << s1 << "+++" << std::endl;

  std::string s2 = VAR4::HString<10>();
  std::cout << s2 << "+++" << std::endl;

  // This will result in an error 
  // std::string s99999 = VAR4::IString<99999>();

  return 0;
}


int main()
{
  //test_indent_1();
  test_indent_2();
  test_indent_3();
  test_indent_4();
  return 0;
}


