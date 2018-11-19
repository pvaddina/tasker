#include "hello.h"
#include <iostream>

SayHello::SayHello(const int native)
{
}

void SayHello::InHindi() const
{
  std::cout << "Namaste" << std::endl;
}

void SayHello::InTelugu() const
{
  std::cout << "Namaskaram" << std::endl;
}

void SayHello::InChinese() const
{
  std::cout << "Nihau" << std::endl;
}

void SayHello::InEnglish() const
{
  std::cout << "Hello" << std::endl;
}

