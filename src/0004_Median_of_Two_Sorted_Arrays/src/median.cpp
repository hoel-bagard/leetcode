#include "median.hpp"

#include <algorithm>
#include <vector>

double Solution::findMedianSortedArrays(std::vector<int>& nums1,
                                        std::vector<int>& nums2) {
  // Initialization some neccessary variables
  std::vector<int> v;

  // store the array in the new array
  for (auto num : nums1)  // O(n1)
    v.push_back(num);

  for (auto num : nums2)  // O(n2)
    v.push_back(num);

  // Sort the array to find the median
  sort(v.begin(), v.end());  // O(nlogn)

  // Find the median and Return it
  long unsigned int n = v.size();  // O(n)

  return n % 2 ? v[n / 2] : (v[n / 2 - 1] + v[n / 2]) / 2.0;
};
