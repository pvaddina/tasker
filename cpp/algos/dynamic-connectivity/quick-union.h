#pragma once

#include <iostream>
#include <vector>
#include <string>

namespace AG
{
  class QuickUnion
  {
    public:
      QuickUnion(const int N)
      {
        for (auto i = 0; i < N; ++i)
        {
          mIds.push_back(i);
        }
      }

      int Root(const int p)
      {
        int i = p;
        while(mIds[i] != i)
        {
          i = mIds[i];
        }
        return i;
      }

      bool Connected(const int p, const int q)
      {
        return Root(p) == Root(q);
      }

      void Union(const int p, const int q)
      {
        mIds[Root(p)] = Root(q);
      }

      void Print(const std::string& s)
      {
        const int N = mIds.size();
        std::cout << s;
        for (auto i = 0; i<N; ++i)
        {
          std::cout << mIds[i] << " ";
        }
        std::cout << std::endl;
      }


    private:
      std::vector<int> mIds;
  };
}
