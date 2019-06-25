#include <iostream>
#include "typname.h"
#include <vector>
#include <string>

int main()
{
  int a;
  std::cout << "a is of type: " << type_name<decltype(a)>() << std::endl;

  char&& c = 'a';
  std::cout << "c is of type: " << type_name<decltype(c)>() << std::endl;

  std::string s;
  std::cout << "s is of type: " << type_name<decltype(s)>() << std::endl;

  std::vector<int> v;
  std::cout << "v is of type: " << type_name<decltype(v)>() << std::endl;

  return 0;
}


