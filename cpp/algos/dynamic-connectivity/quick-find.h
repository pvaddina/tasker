#pragma once

#include <iostream>
#include <vector>
#include <string>

namespace AG
{
  class QuickFind
  {
    public:
      QuickFind(const int N)
      {
        for (auto i = 0; i < N; ++i)
        {
          mIds.push_back(i);
        }
      }

      bool Connected(const int p, const int q)
      {
        return mIds[p] == mIds[q];
      }

      void Union(const int p, const int q)
      {
        const int id2Change = mIds[p];
        const int targetId = mIds[q];
        const int N = mIds.size();
        mIds[p] = targetId;
        for (auto i = 0; i<N; ++i)
        {
          if (mIds[i] == id2Change)
          {
            mIds[i] = targetId;
          }
        }
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
