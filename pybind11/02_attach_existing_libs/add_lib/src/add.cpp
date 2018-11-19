#include "add.h"
#include <iostream>

int add(const int iOne, const int iTwo)
{
  std::cout << "Adding the numbers " << iOne << ", and " << iTwo << std::endl;
  return iOne + iTwo;
}

