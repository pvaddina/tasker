#pragma once

#include <iostream>
#include <vector>
#include <string>

namespace AG
{
  class QuickUnionWtPathComp
  {
    public:
      QuickUnionWtPathComp(const int N)
      {
        for (auto i = 0; i < N; ++i)
        {
          mIds.push_back(i);
          mWeights.push_back(1); // At the beginning all the weights are just 1
        }
      }

      // Get the parent of the current parent, and set it as the new parent
      // Over time this will result in a shorter tree.
      //                2
      //              /   \
      //             4     7
      //            /
      //           5
      //          / \
      //         9   3 
      // In the figure above when p = 3;
      // Loop-1: i = 3; mIds[3] = 5; Inside the loop, mIds[3] = mIds[mIds[3]] = mIds[5] = 4; 
      //         After the end of loop-1, '4' will be the root of the item, '3'
      //                2
      //              /   \
      //             4     7
      //            / \
      //           5   3
      //          / 
      //         9   
      // Loop-2: i = 4; mIds[4] = 2; Again, mIds[4] = mIds[mIds[4]] = mIds[2] = 2; 
      //         After this loop the value of root of '4' does not change. But if there were something
      //         else as the root of 2, then it could be have been the new root. 
      int Root(const int p)
      {
        int i = p;
        while(mIds[i] != i)
        {
          mIds[i] = mIds[mIds[i]];
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
        auto rootP = Root(p);
        auto rootQ = Root(q);

        // This function will perform a union of P, with Q.
        // Meaning after this operation, the tree with P as root
        // will go under/connect to the tree with Q as root. 
        // Therefore, the new weight of P will will be 0, 
        // and the weight of Q will increase by the weight of P.
        auto unionP2Q = [&](const int p, const int q) {
          mIds[p] = mIds[q];
          mWeights[q] += mWeights[p];
          mWeights[p] = 0;
        };

        if (mWeights[rootP] >= mWeights[rootQ])
        {
          unionP2Q(rootQ, rootP);
        }
        else
        {
          unionP2Q(rootP, rootQ);
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
        std::cout << "; Weights= ";
        for (auto i = 0; i<N; ++i)
        {
          std::cout << mWeights[i] << " ";
        }
        std::cout << std::endl;
      }

    private:
      std::vector<int> mIds;
      std::vector<int> mWeights; // Weights of all items, where a weight indicates 
                                 // the number of items under it as children. At 
                                 // the very beginning there is just one item at 
                                 // each index. Therefore, each item contains a value 1
  };
}
